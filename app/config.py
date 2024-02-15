
import os

ROOT_PATH=os.path.dirname(os.path.abspath(__file__))+'/'


## Flask 設定
UPLOAD_FOLDER =ROOT_PATH+"uploads/"
FLASK_PORT = 8888
FLASK_STATIC_DIR = ROOT_PATH+"static/"

## 網站設定 
FILESYSTEM = ROOT_PATH+'templates/'



## 網站資料

PAGES=[
        ["index","首頁"],
        ["what","什麼是附帶決議"],
        ["story","本土小牙醫故事"],    
        ["news-detail","最新消息"],
        ["links","相關資訊"],
        ["contact","聯絡我們"]
]
"""
[route, title]
"""

PAGE_TITLE={
    page[0]:page[1] for page in PAGES 
}
"""
route -> title
"""

WEBSITE_INFO={
    "title":"TGDPA",
    "subtitle":"Taiwan General Dental Practitioners Association",
    "tel":"tel number???",
    "email":"email???",
    "address":"地址???",
    "copyright":"??? 2023",
    
    
    "pages":PAGES,
    "socials":[
        ["facebook","https://www.facebook.com/"],
        ["youtube","https://www.youtube.com/"]
    ],



    "color1":"red",


    "origin":"hihihi"

}


## QA 資料
QA_CONTENT=ROOT_PATH+'contents/qa.csv'
QA_FIG_DIR='images/qa/'

## News 資料
NEWS_DIR=ROOT_PATH+'/contents/news/'
