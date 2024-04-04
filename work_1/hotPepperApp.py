# モジュールを呼び出し
import requests
import tkinter as tk
import mapApp as ma

def hotPepperApp(area, keyword):
    # リクエストURLを変数へ格納
    URL = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'
    # APIキーを変数へ格納
    API_KEY = '8c4b2c249c045178'

    #リクエストするデータの情報を辞書で作成
    body = {
        'key' : API_KEY,
        'address' : area,
        'keyword' : keyword,
        'format' : 'json',
        'count' : 15
    }

    # bodyの情報をもとにrequestsライブラリでAPIへリクエスト
    # 取得したデータをresponse変数へ格納
    response = requests.get(URL,body)

    # 取得したデータからJSONデータを取得
    area_data = response.json()
    # JSONデータからお店のデータを取得
    stores = area_data['results']['shop']

    # 結果表示ウインドウを作成
    root = tk.Tk()
    root.attributes("-topmost", True)
    # ウインドウサイズ設定
    root.geometry("1200x400")
    # ウインドウ背景色設定
    root.configure(bg="darkblue")
    # フレームを作成
    frame = tk.Frame(root)
    # ラベルを作成
    lbl = tk.Label(text="検索結果", font=("HG丸ｺﾞｼｯｸM-PRO", 18,), bg="darkblue", fg="white")
    # 検索結果を表示するリストボックスを作成
    result = tk.Listbox(root, width=100, height=20, font=("HG丸ｺﾞｼｯｸM-PRO",12), bg="orange")
    # 店名と住所をリストから抜き出してリストボックスへ追加していく
    store_address =[]
    for store_name in stores:
        name = store_name['name']
        address = store_name['address']
        i = 0
        store_address.append(address)
        store = f"【{name}】［{address}］"
        result.insert(i,store)
        i += 1
    # ウインドウを閉じる処理
    def click_close():
        root.destroy()
    # 「Map」ボタンを押したときの処理
    def button_push():
        # 選択したリストアイテムを取得
        # 選択されたデータのインデックスを取得
        selected_index = result.curselection()
        selected_store_name = result.get(selected_index[0])
        for index_num in selected_index:
            selected_index_int = int(index_num)
        # インデックスを元にデータを取得
        selected_store = store_address[selected_index_int]
        # ウインドウを閉じる
        click_close()
        # 選択した店名を引数にして関数を呼び出し
        ma.mapApp(selected_store, selected_store_name)
    # 「Map」ボタンを作成
    btn = tk.Button(text="Map", width=10, bg="white", fg="orange", font = ("HG丸ｺﾞｼｯｸM-PRO",16), command= button_push)


    lbl.pack()
    frame.pack()
    result.pack(pady=10)
    btn.place(x=535, y=330)
    root.protocol("WM_DELETE_WINDOW", click_close)
    tk.mainloop()

    



