# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## プロジェクト概要

html2md-web: WebページをMarkdownに変換するFlask Webアプリケーション。
CLI対応のコンバーターモジュールとWeb UIを提供。

## コマンド

```bash
# 仮想環境の有効化
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 依存パッケージのインストール
pip install -r requirements.txt

# 開発サーバー起動
python app.py

# CLI使用
python converter.py <URL> [-o output.md] [-s selector] [-t timeout]
```

## アーキテクチャ

- **app.py**: Flaskメインアプリケーション
  - `GET /`: Web UI（Bootstrap 5）
  - `POST /api/convert`: 変換API
  - `GET /api/selectors`: セレクタ一覧API

- **converter.py**: HTML→Markdown変換ロジック
  - `convert_url(url, custom_selector, timeout)`: メイン変換関数
  - `ConversionResult`: 変換結果データクラス
  - `SITE_SELECTORS`: サイト別セレクタ設定
  - `parse_selector(selector_str)`: セレクタ文字列パーサー
  - CLI対応（argparse）

- **templates/**: Jinja2テンプレート
  - `base.html`: ベーステンプレート（Bootstrap 5 CDN）
  - `index.html`: メインページ（入力フォーム、結果表示）
  - `404.html`: エラーページ

- **static/css/**: カスタムCSS

## サイト別セレクタ

`converter.py`の`SITE_SELECTORS`辞書で管理。新しいサイトを追加する場合：

```python
SITE_SELECTORS = {
    "site_name": {
        "domains": ["example.com"],
        "selector": ("div", {"class_": "content"}),
    },
    # ...
}
```

## 依存関係

- Python 3.13.1 (pyenv管理)
- requests: HTTP通信
- beautifulsoup4: HTML解析
- markdownify: HTML→Markdown変換
- Flask: Webフレームワーク
