# モジュールを呼び出し
import requests
import folium
import googlemaps
import webview

# 地図を作成する関数
def mapApp(selected_store, selected_store_name):
    # Google Map javascript APIへアクセスして住所から緯度・経度を取得
    API_KEY = 'AIzaSyDa5XBlME_4fCZr1SlBYlVXNCHooM3q6mc'
    gm = googlemaps.Client(API_KEY)
    res = gm.geocode(f'{selected_store}')
    
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={selected_store}&key={API_KEY}'

    res = requests.get(url)
    location = res.json()["results"][0]["geometry"]["location"]
    lat = location["lat"]
    lng = location["lng"]

    # 取得した緯度・経度から地図を作成
    maps = folium.Map(location= [lat, lng], zoom_start=16, width = 1000, height = 600)
    folium.Marker([lat, lng], tooltip=selected_store_name).add_to(maps)
    # HTMLファイルを作成して保存
    maps.save('map.html')
    # ウインドウを作ってHTMLファイルを表示
    webview.create_window('Map', 'map.html', width=1000, height=600)
    webview.start() 