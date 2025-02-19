import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

def fetch_and_convert(url):
    # URLからHTMLを取得
    response = requests.get(url)
    response.raise_for_status()
    
    # BeautifulSoupでHTMLを解析
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 本文の抽出（適宜セレクタを調整してください）
    # content = soup.find('div', class_='entry-content') # はてなブログ
    # content = soup.find('div', class_='note-common-styles__textnote-body') # note.com
    # content = soup.find('div', class_='View_main__AU6KW') # zenn.dev
    content = soup.find('div', class_='bg-white p-4 md:p-6') # dev.classmethod.jp
    
    if content:
        # HTMLをMarkdownに変換
        markdown = md(str(content))
        with open('output.md', 'w', encoding='utf-8') as f:
            f.write(markdown)
        print("Markdownファイルに変換しました。")
    else:
        # 本文が見つからない場合
        print("本文が見つかりませんでした。選択したセレクタが正しいか確認してください。")

if __name__ == "__main__":
    # 処理を開始するURL
    url = 'https://dev.classmethod.jp/articles/aws-hands-on-for-beginners-serverless2/'
    fetch_and_convert(url)
