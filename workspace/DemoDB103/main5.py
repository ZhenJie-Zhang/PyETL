import requests
import os
from bs4 import BeautifulSoup
import warnings

warnings.filterwarnings('ignore')

url = "https://www.ptt.cc/bbs/Beauty/M.1565481224.A.300.html"
response = requests.get(url, cookies={"over18": "1"}).text
# 如果是requests，多一個步驟，.text欄位拿出
html = BeautifulSoup(response)

metas = html.find_all("span", class_="article-meta-value")
print("ID", metas[0].text)
print("看板", metas[1].text)
print("標題", metas[2].text)
print("時間", metas[3].text)
pushes = html.find_all("span", class_="push-tag")
score = 0
for p in pushes:
    if "推" in p.text:
        score += 1
    elif "嘘" in p.text:
        score -= 1
print(score)
saved = {"id": metas[0],
         "board": metas[1],
         "title": metas[2],
         "time": metas[3],
         "score": score}


notallowed = '/|\?"*:<>.'

title_revised = ""

for i, a in enumerate(html.find_all("a")):
    allow = ["gif", "jpg", "jpeg", "png"]
    if a["href"].split(".")[-1].lower() in allow:
        print(a["href"])
        # .raw(圖片...):steam=True
        img_response = requests.get(a["href"], stream=True)
        img = img_response.raw.read()

        dn = "ptt"
        fn = dn + "/" + str(i) + "." + a["href"].split(".")[-1]
        if not os.path.exists(dn):
            os.makedirs(dn)
        f = open(fn, "wb")
        f.write(img)
        f.close()
