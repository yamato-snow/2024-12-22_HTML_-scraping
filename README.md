# html2md-web

WebページをMarkdownに変換するFlask Webアプリケーション。

## 機能

- URLを入力してMarkdownに変換
- 複数サイトの自動セレクタ判定
- カスタムセレクタ指定
- Markdown結果のコピー/ダウンロード
- RESTful API

## セットアップ

### 前提条件

- Python 3.13+
- pip

### インストール

```bash
# リポジトリのクローン
git clone https://github.com/yamato-snow/html2md-web.git
cd html2md-web

# 仮想環境の作成・有効化
python -m venv .venv

# Windows:
.venv\Scripts\activate

# macOS/Linux:
source .venv/bin/activate

# 依存パッケージのインストール
pip install -r requirements.txt
```

### 実行

```bash
# 開発サーバー起動
python app.py

# http://localhost:5000 でアクセス
```

## 使い方

### Web UI

1. ブラウザで http://localhost:5000 を開く
2. URLを入力
3. (オプション) カスタムセレクタを指定
4. 「変換」ボタンをクリック
5. 結果をコピーまたはダウンロード

### CLI

```bash
# 基本的な使い方
python converter.py https://example.com/article

# ファイルに出力
python converter.py https://example.com/article -o output.md

# カスタムセレクタ指定
python converter.py https://example.com/article -s "div.content"

# タイムアウト指定
python converter.py https://example.com/article -t 60
```

### API

#### POST /api/convert

URLをMarkdownに変換します。

**Request:**
```json
{
    "url": "https://example.com/article",
    "selector": "div.content"
}
```

**Response (成功):**
```json
{
    "success": true,
    "data": {
        "markdown": "# Title\n\nContent...",
        "title": "Article Title",
        "url": "https://example.com/article",
        "selector_used": "default"
    }
}
```

**Response (エラー):**
```json
{
    "success": false,
    "error": "エラーメッセージ"
}
```

#### GET /api/selectors

サポートされているセレクタ一覧を取得します。

**Response:**
```json
{
    "selectors": [
        {
            "name": "hatenablog",
            "domains": ["hatenablog.com", "hatenablog.jp", "hateblo.jp"],
            "selector": "div.entry-content"
        }
    ]
}
```

## 自動判定対応サイト

| サイト | ドメイン |
|--------|----------|
| はてなブログ | hatenablog.com, hatenablog.jp, hateblo.jp |
| note | note.com |
| Zenn | zenn.dev |
| Qiita | qiita.com |
| Classmethod | dev.classmethod.jp |
| Cursor | cursor.com |
| くらしとノーション | kurashi-notion.com |
| Protopedia | protopedia.net |
| BizHint | bizhint.jp |
| INC Design | incdesign.jp |
| WEEL | weel.co.jp |
| SB Bit | sbbit.jp |
| DreamNews | dreamnews.jp |

その他のサイトは `main` タグをデフォルトで使用します。

## プロジェクト構成

```
html2md-web/
├── app.py              # Flaskメインアプリ
├── converter.py        # 変換ロジック
├── templates/
│   ├── base.html      # ベーステンプレート
│   ├── index.html     # メインページ
│   └── 404.html       # 404エラーページ
├── static/
│   └── css/
│       └── style.css  # カスタムスタイル
├── .gitignore
├── .python-version
├── README.md
├── CLAUDE.md
└── requirements.txt
```

## ライセンス

MIT License
