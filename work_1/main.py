# モジュールを呼び出し
from bottle import route, run, template, static_file, request
import os
from hotPepperApp import hotPepperApp

# Styleシートと画像をHTMLから読み込めるように設定
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR,'static')

@route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./static')

# GourmetSearchサイトにアクセスしたらページを作成
@route('/gourmetsearch')
def gourmetSearch():
    return template('gourmetsearch', input_text1="",input_text2="")

# 検索ボタンを押したら、検索ワードを保持して関数呼び出し
@route('/gourmetsearch', method='POST')
def do_gourmetSearch():
    area = request.forms.getunicode('input_text1')
    keyword = request.forms.getunicode('input_text2')
    hotPepperApp(area, keyword)
# 開発サーバー起動
run(host='localhost', port=8080, debug=True)

