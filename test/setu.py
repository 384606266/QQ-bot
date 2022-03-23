#利用国内url的涩图爬虫
from email import header
import requests
import json
from pathlib import Path

def get_img():
    url = 'https://api.lolicon.app/setu/v2?r18=1'
    r = requests.get(url)
    dic = r.json()

    pic_title = dic["data"][0]["title"]
    pic_url = dic["data"][0]["urls"]["original"]
    pic_pid = dic["data"][0]["pid"]
    pic_author = dic["data"][0]["author"]
    print(pic_url)
    
    img = requests.get(pic_url, headers=header).content
    img_path = "imgs\\" + pic_title + ".jpg"
    with open(img_path) as file:
        file.write(img)
        
get_img()