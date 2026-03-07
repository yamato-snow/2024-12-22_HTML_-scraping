"""
HTML to Markdown Converter Module

WebページのHTMLを取得し、Markdown形式に変換するモジュール。
サイト別のセレクタ自動判定機能付き。
"""
import argparse
import sys
from dataclasses import dataclass
from typing import Optional
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md


@dataclass
class ConversionResult:
    """変換結果を格納するデータクラス"""
    success: bool
    markdown: Optional[str] = None
    title: Optional[str] = None
    url: Optional[str] = None
    error: Optional[str] = None
    selector_used: Optional[str] = None

    def to_dict(self) -> dict:
        """辞書形式に変換"""
        return {
            "success": self.success,
            "markdown": self.markdown,
            "title": self.title,
            "url": self.url,
            "error": self.error,
            "selector_used": self.selector_used,
        }


# サイト別セレクタ設定
SITE_SELECTORS: dict = {
    "hatenablog": {
        "domains": ["hatenablog.com", "hatenablog.jp", "hateblo.jp"],
        "selector": ("div", {"class_": "entry-content"}),
    },
    "note": {
        "domains": ["note.com"],
        "selector": ("div", {"class_": "note-common-styles__textnote-body"}),
    },
    "zenn": {
        "domains": ["zenn.dev"],
        "selector": ("div", {"class_": "View_main__AU6KW"}),
    },
    "qiita": {
        "domains": ["qiita.com"],
        "selector": ("div", {"class_": "p-items_main"}),
    },
    "classmethod": {
        "domains": ["dev.classmethod.jp"],
        "selector": ("div", {"class_": "bg-white p-4 md:p-6"}),
    },
    "cursor": {
        "domains": ["cursor.com"],
        "selector": ("main", {}),
    },
    "kurashi_notion": {
        "domains": ["kurashi-notion.com"],
        "selector": ("div", {"id": "shopify-section-template--23575026860308__main"}),
    },
    "protopedia": {
        "domains": ["protopedia.net"],
        "selector": ("main", {}),
    },
    "bizhint": {
        "domains": ["bizhint.jp"],
        "selector": ("body", {}),
    },
    "incdesign": {
        "domains": ["incdesign.jp"],
        "selector": ("div", {"id": "mainContent"}),
    },
    "weel": {
        "domains": ["weel.co.jp"],
        "selector": ("div", {"id": "content"}),
    },
    "sbbit": {
        "domains": ["sbbit.jp"],
        "selector": ("main", {"class_": "cnt_main--v2"}),
    },
    "dreamnews": {
        "domains": ["dreamnews.jp"],
        "selector": ("div", {"id": "colmunLeft"}),
    },
    # フォールバック
    "default": {
        "domains": [],
        "selector": ("main", {}),
    },
}


def get_selector_for_url(url: str) -> tuple:
    """
    URLからドメインを解析し、適切なセレクタを返す

    Args:
        url: 対象URL

    Returns:
        tuple: (tag_name, attrs_dict, selector_name)
    """
    parsed = urlparse(url)
    domain = parsed.netloc.lower()

    for name, config in SITE_SELECTORS.items():
        if name == "default":
            continue
        for site_domain in config["domains"]:
            if site_domain in domain:
                tag, attrs = config["selector"]
                return tag, attrs, name

    # デフォルトフォールバック
    tag, attrs = SITE_SELECTORS["default"]["selector"]
    return tag, attrs, "default"


def fetch_html(url: str, timeout: int = 30) -> tuple:
    """
    URLからHTMLを取得

    Args:
        url: 対象URL
        timeout: タイムアウト秒数

    Returns:
        tuple: (html_content, error_message)
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        response.encoding = response.apparent_encoding or 'utf-8'
        return response.text, None
    except requests.exceptions.Timeout:
        return "", f"タイムアウト: {timeout}秒以内に応答がありませんでした"
    except requests.exceptions.ConnectionError:
        return "", "接続エラー: URLに接続できませんでした"
    except requests.exceptions.HTTPError as e:
        return "", f"HTTPエラー: {e.response.status_code}"
    except requests.exceptions.RequestException as e:
        return "", f"リクエストエラー: {str(e)}"


def extract_content(html: str, tag: str, attrs: dict) -> tuple:
    """
    HTMLから本文を抽出

    Args:
        html: HTMLコンテンツ
        tag: 抽出対象のタグ名
        attrs: 抽出対象の属性

    Returns:
        tuple: (content_html, title)
    """
    soup = BeautifulSoup(html, 'html.parser')

    # タイトル取得
    title_tag = soup.find('title')
    title = title_tag.get_text(strip=True) if title_tag else None

    # 本文抽出
    if attrs:
        content = soup.find(tag, **attrs)
    else:
        content = soup.find(tag)

    if content:
        return str(content), title

    # フォールバック: bodyタグを試行
    body = soup.find('body')
    if body:
        return str(body), title

    return None, title


def convert_to_markdown(html_content: str) -> str:
    """
    HTMLをMarkdownに変換

    Args:
        html_content: HTMLコンテンツ

    Returns:
        str: Markdown形式のテキスト
    """
    return md(html_content, heading_style="ATX", strip=['script', 'style'])


def convert_url(url: str, custom_selector: Optional[tuple] = None, timeout: int = 30) -> ConversionResult:
    """
    URLからMarkdownに変換するメイン関数

    Args:
        url: 変換対象のURL
        custom_selector: カスタムセレクタ (tag, attrs) のタプル
        timeout: リクエストタイムアウト秒数

    Returns:
        ConversionResult: 変換結果
    """
    # URL検証
    if not url or not url.startswith(('http://', 'https://')):
        return ConversionResult(
            success=False,
            url=url,
            error="無効なURL形式です。http:// または https:// で始まるURLを指定してください"
        )

    # セレクタ決定
    if custom_selector:
        tag, attrs = custom_selector
        selector_name = "custom"
    else:
        tag, attrs, selector_name = get_selector_for_url(url)

    # HTML取得
    html, error = fetch_html(url, timeout)
    if error:
        return ConversionResult(
            success=False,
            url=url,
            error=error,
            selector_used=selector_name
        )

    # 本文抽出
    content_html, title = extract_content(html, tag, attrs)
    if not content_html:
        return ConversionResult(
            success=False,
            url=url,
            title=title,
            error="本文を抽出できませんでした。セレクタを変更してみてください",
            selector_used=selector_name
        )

    # Markdown変換
    markdown = convert_to_markdown(content_html)

    return ConversionResult(
        success=True,
        markdown=markdown,
        title=title,
        url=url,
        selector_used=selector_name
    )


def convert_html(html: str, custom_selector: Optional[tuple] = None, filename: Optional[str] = None) -> ConversionResult:
    """
    HTML文字列からMarkdownに変換する関数

    Args:
        html: HTMLコンテンツ文字列
        custom_selector: カスタムセレクタ (tag, attrs) のタプル
        filename: アップロードされたファイル名

    Returns:
        ConversionResult: 変換結果
    """
    if not html or not html.strip():
        return ConversionResult(
            success=False,
            error="HTMLコンテンツが空です"
        )

    # セレクタ決定
    if custom_selector:
        tag, attrs = custom_selector
        selector_name = "custom"
    else:
        tag, attrs = SITE_SELECTORS["default"]["selector"]
        selector_name = "default"

    # 本文抽出
    content_html, title = extract_content(html, tag, attrs)
    if not content_html:
        return ConversionResult(
            success=False,
            title=title,
            error="本文を抽出できませんでした。セレクタを変更してみてください",
            selector_used=selector_name
        )

    # Markdown変換
    markdown = convert_to_markdown(content_html)

    return ConversionResult(
        success=True,
        markdown=markdown,
        title=title or filename,
        selector_used=selector_name
    )


def parse_selector(selector_str: str) -> Optional[tuple]:
    """
    セレクタ文字列をパースして(tag, attrs)タプルに変換

    Args:
        selector_str: セレクタ文字列（例: "div.content", "main", "article#post"）

    Returns:
        tuple: (tag, attrs) または None
    """
    if not selector_str:
        return None

    selector_str = selector_str.strip()

    # クラスセレクタ: "div.classname"
    if '.' in selector_str:
        parts = selector_str.split('.', 1)
        tag = parts[0] or 'div'
        cls = parts[1]
        return (tag, {"class_": cls})

    # IDセレクタ: "div#id"
    if '#' in selector_str:
        parts = selector_str.split('#', 1)
        tag = parts[0] or 'div'
        id_val = parts[1]
        return (tag, {"id": id_val})

    # タグのみ: "main"
    return (selector_str, {})


def main():
    """CLI エントリーポイント"""
    parser = argparse.ArgumentParser(
        description="HTMLをMarkdownに変換するツール",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用例:
  python converter.py https://example.com/article
  python converter.py https://example.com/article -o output.md
  python converter.py https://example.com/article -s "div.content"
        """
    )
    parser.add_argument("url", help="変換対象のURL")
    parser.add_argument(
        "-o", "--output",
        help="出力ファイルパス（省略時は標準出力）"
    )
    parser.add_argument(
        "-s", "--selector",
        help="カスタムセレクタ（例: 'div.content', 'main', 'article#post'）"
    )
    parser.add_argument(
        "-t", "--timeout",
        type=int,
        default=30,
        help="リクエストタイムアウト秒数（デフォルト: 30）"
    )

    args = parser.parse_args()

    # カスタムセレクタのパース
    custom_selector = parse_selector(args.selector)

    # 変換実行
    result = convert_url(args.url, custom_selector, args.timeout)

    if not result.success:
        print(f"エラー: {result.error}", file=sys.stderr)
        sys.exit(1)

    # 出力テキスト生成
    output_text = result.markdown
    if result.title:
        output_text = f"# {result.title}\n\n{result.markdown}"

    # ファイル出力または標準出力
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output_text)
        print(f"変換完了: {args.output}")
        print(f"使用セレクタ: {result.selector_used}")
    else:
        print(output_text)


if __name__ == "__main__":
    main()
