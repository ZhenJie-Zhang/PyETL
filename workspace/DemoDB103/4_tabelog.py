from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "https://tabelog.com/tw/tokyo/rstLst/?SrtT=rt"
response = urlopen(url)
# 檔案 -> 最外面的盒子<html>
html = BeautifulSoup(response)
# html.find_all("li", {"class":"list-rst"})
rs = html.find_all("li", class_="list-rst")
# rs是一個盒子list, 不是一個盒子
for r in rs:
    ja = r.find("small", class_="list-rst__name-ja")
    en = r.find("a", class_="list-rst__name-main")
    rating = r.find("b", class_="c-rating__val")
    prices = r.find_all("span", class_="c-rating__val")
    # 萃取紙條: 盒子.text
    # 萃取特徵: 盒子["href"]
    print(rating.text, en.text, ja.text)
    print("晚間價錢:", prices[0].text)
    print("午間價錢:", prices[1].text)
    print(en["href"])