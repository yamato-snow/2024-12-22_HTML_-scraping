"""
HTML to Markdown Web Application

Flask を使用したWebアプリケーション。
URLを入力してMarkdownに変換するWeb UIとREST APIを提供。
"""
from flask import Flask, render_template, request, jsonify
from converter import convert_url, parse_selector, SITE_SELECTORS

app = Flask(__name__)

# 設定
app.config['JSON_AS_ASCII'] = False  # 日本語対応
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB制限


@app.route('/')
def index():
    """メインページ"""
    # サポートサイト一覧を渡す
    supported_sites = [
        {"name": name, "domains": config["domains"]}
        for name, config in SITE_SELECTORS.items()
        if config["domains"]  # defaultを除外
    ]
    return render_template('index.html', supported_sites=supported_sites)


@app.route('/api/convert', methods=['POST'])
def api_convert():
    """
    API: URLをMarkdownに変換

    Request Body (JSON):
        {
            "url": "https://example.com/article",
            "selector": "div.content"  // optional
        }

    Response (JSON):
        {
            "success": true,
            "data": {
                "markdown": "# Title\n...",
                "title": "Article Title",
                "url": "https://...",
                "selector_used": "default"
            }
        }
        or
        {
            "success": false,
            "error": "エラーメッセージ"
        }
    """
    # リクエスト検証
    if not request.is_json:
        return jsonify({
            "success": False,
            "error": "Content-Type must be application/json"
        }), 400

    data = request.get_json()
    url = data.get('url', '').strip()
    selector = data.get('selector', '').strip() or None

    if not url:
        return jsonify({
            "success": False,
            "error": "URLは必須です"
        }), 400

    # カスタムセレクタのパース
    custom_selector = parse_selector(selector)

    # 変換実行
    result = convert_url(url, custom_selector)

    if result.success:
        return jsonify({
            "success": True,
            "data": {
                "markdown": result.markdown,
                "title": result.title,
                "url": result.url,
                "selector_used": result.selector_used
            }
        })
    else:
        return jsonify({
            "success": False,
            "error": result.error
        }), 400


@app.route('/api/selectors', methods=['GET'])
def api_selectors():
    """API: サポートされているセレクタ一覧"""
    selectors = []
    for name, config in SITE_SELECTORS.items():
        tag, attrs = config["selector"]
        selector_str = tag
        if attrs.get("class_"):
            selector_str += f".{attrs['class_']}"
        elif attrs.get("id"):
            selector_str += f"#{attrs['id']}"

        selectors.append({
            "name": name,
            "domains": config["domains"],
            "selector": selector_str
        })
    return jsonify({"selectors": selectors})


@app.errorhandler(404)
def not_found(e):
    """404エラーハンドラ"""
    if request.path.startswith('/api/'):
        return jsonify({"success": False, "error": "Not Found"}), 404
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    """500エラーハンドラ"""
    return jsonify({"success": False, "error": "Internal Server Error"}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5100)
