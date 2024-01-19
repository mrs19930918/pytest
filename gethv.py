from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# 適切な待機時間を設定
def wait():
    time.sleep(2)  # 例: 2秒待機

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_article', methods=['POST'])
def get_article():
    url = request.form['url']

    # ページの取得
    response = requests.get(url)
    
    # HTMLの解析
    soup = BeautifulSoup(response.text, 'html.parser')

    # 見出しの取得
    headings = soup.find_all(['h1', 'h2', 'h3'])  # 適切な見出しタグを指定
    title = headings[0].text if headings else 'No Title'

    # 埋め込み動画のURLの取得
    video_embed = soup.find('iframe')  # 適切なセレクタを指定
    video_url = video_embed['src'] if video_embed else 'No Video'

    return render_template('article.html', title=title, video_url=video_url)

if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=False)