#使用BeautifulSoup解析Pixiv，但还没做反爬，暂时不可用

import requests
from bs4 import BeautifulSoup  # HTML/XML解析库
import urllib

from sympy import re

def GetByID (id):
    url = "https://www.pixiv.net/users/" + id
    
    print(url)
    idpage = requests.get(url)
    idsoup = BeautifulSoup(idpage.content, "lxml")
    print(idpage.content.decode())
'''
    box = idsoup.find('ul', class_ = "sc-9y4be5-1 jtUPOE")
    for li in box.find_all('li'):
        for link in li.find_all('a'):
            link_ = link.get('herf')
            chara_page = requests.get(link_)
            chara_soup = BeautifulSoup(chara_page.content, 'lxml')
            print(chara_page.content.decode())
'''
GetByID("10670214")