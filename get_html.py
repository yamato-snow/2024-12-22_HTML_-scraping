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
    # content = soup.find('div', class_='bg-white p-4 md:p-6') # dev.classmethod.jp
    # content = soup.find('div', id='shopify-section-template--23575026860308__main') # kurashi-notion.com
    # content = soup.find('main') # protopedia.net
    # content = soup.find('body') # bizhint.jp
    # content = soup.find('div', id='mainContent') # incdesign.jp
    # content = soup.find('div', class_='article-main')
    # content = soup.find('div', id='content') # weel.co.jp
    content = soup.find('div', class_='p-items_main') # qiita.com
    # content = soup.find('main', class_='cnt_main--v2') # sbbit.jp
    # content = soup.find('div', id='colmunLeft') # dreamnews.jp

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
    url = 'https://qiita.com/tichise/items/6c4a21d47dc7ee0968eb'
    fetch_and_convert(url)
