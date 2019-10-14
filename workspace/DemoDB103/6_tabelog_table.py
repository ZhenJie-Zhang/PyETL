from urllib.request import urlopen
from bs4 import BeautifulSoup
# Step0 : import
import pandas as pd
# Step1: 準備空表格(columns:會先固定住欄位順序)
df = pd.DataFrame(columns=["評價", "日文", "英文", "詳細"])
page = 51
while True:
    print("目前第幾頁?", page)
    url = "https://tabelog.com/tw/tokyo/rstLst/" + str(page) + "/?SrtT=rt"
    try:
        response = urlopen(url)
    except:
        print("應該是到底了吧")
        # Step4. 儲存檔案
        # index=False, 不要儲存0,1,2....
        df.to_csv("tabelog.csv",
                  encoding="utf-8",
                  index=False)
        break
    html = BeautifulSoup(response)
    rs = html.find_all("li", class_="list-rst")
    for r in rs:
        ja = r.find("small", class_="list-rst__name-ja")
        en = r.find("a", class_="list-rst__name-main")
        rating = r.find("b", class_="c-rating__val")
        prices = r.find_all("span", class_="c-rating__val")
        print(rating.text, en.text, ja.text)
        print("晚間價錢:", prices[0].text)
        print("午間價錢:", prices[1].text)
        print(en["href"])
        # Step2. 準備要插入的資料
        data = {"評價":rating.text,
                "日文":ja.text,
                "英文":en.text,
                "詳細":en["href"]}
        # Step3. 插入進去(append)
        # 只要是dataframe專屬功能, 都是屬於第一種(有兩份)
        df = df.append(data, ignore_index=True)
    page = page + 1
