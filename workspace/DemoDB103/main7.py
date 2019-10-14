import requests
from bs4 import BeautifulSoup
import json

start = 0
page = 0
while True:
    url = "https://www.google.com/search?ei=sS9nXYf0FYXomAWatI_wAw&rlz=1C1SQJL_zh-TWTW836TW836&yv=3&newwindow=1&tbm=isch&q=%E7%A6%8F%E5%8E%9F%E7%B6%BE%E9%A6%99&vet=10ahUKEwjHkPD7-6bkAhUFNKYKHRraAz4QuT0INigB.sS9nXYf0FYXomAWatI_wAw.i&ved=0ahUKEwjHkPD7-6bkAhUFNKYKHRraAz4QuT0INigB&ijn="\
          + str(page) + "&start=" \
          + str(page) * 100 + "0&asearch=ichunk&async=_id:rg_s,_pms:s,_jsfs:Ffpdje,_fmt:pc"
    page += 1

    headers = {
        "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    response = requests.get(url, headers=headers)
    html = BeautifulSoup(response.text)
    pictures = html.find_all("div", class_="rg_meta")
    if len(pictures) == 0:
        print("沒有圖檔")
        break


    for p in pictures:
        data = json.loads(p.text)
        print("類型", data["ity"])
        print("標題", data["pt"])
        print("圖片", data["ou"])
        print("第幾張", start)
        try:
            response = requests.get(data["ou"], stream=True)
            if data["ity"] == "":
                fn = "FukuharaAyaka/" + str(start) + ".jpg"
            else:
                fn = "FukuharaAyaka/" + str(start) + "." + data["ity"]
            f = open(fn, "wb")
            f.write(response.raw.read())
            f.close()
            start += 1

        except:
            print("不能下載")
