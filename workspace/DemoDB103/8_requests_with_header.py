import requests
from bs4 import BeautifulSoup
import os
import json
url = "https://www.ptt.cc/bbs/Beauty/M.1566564345.A.15F.html"
response = requests.get(url, cookies={"over18":"1"})
# 如果是requests, 多一個步驟, .text欄位拿出
html = BeautifulSoup(response.text)

# 作者. 標題. 發文時間
metas = html.find_all("span", class_="article-meta-value")
print("ID:", metas[0].text)
print("看板:", metas[1].text)
print("標題:", metas[2].text)
print("時間:", metas[3].text)
score = 0
pushes = html.find_all("span", class_="push-tag")
for p in pushes:
    if "推" in p.text:
        score = score + 1
    elif "噓" in p.text:
        score = score - 1
print("推噓文分數:", score)

saved = {"id":metas[0].text,
         "board":metas[1].text,
         "title":metas[2].text,
         "date":metas[3].text,
         "score":score}

# 圖片部分
# 準備一下我們儲存資料夾(你不能把title拿來當資料夾)
# 要先把資料夾不允許的字去掉
notallowed = ["/", "|", "\\", "?",
              "\"", "*", ":", "<",
              ">", "."]
title_revised = ""
for c in metas[2].text:
    if not c in notallowed:
        title_revised = title_revised + c

for i, a in enumerate(html.find_all("a")):
    allow = ["gif", "jpg", "jpeg", "png"]
    if a["href"].split(".")[-1].lower() in allow:
        print("[下載圖片]:", a["href"])
        # .raw(圖片...): stream = True
        img_response = requests.get(a["href"], stream=True)
        img = img_response.raw.read()

        dn = "ptt/" + title_revised
        fn = dn + "/" + str(i) + "." + a["href"].split(".")[-1]
        if not os.path.exists(dn):
            os.makedirs(dn)
        f = open(fn, "wb")
        f.write(img)
        f.close()

# 內文(刪除不必要)
content = html.find("div", id="main-content")
ds = content.find_all("div", class_="article-metaline")
for d in ds:
    d.extract()
ds = content.find_all("div", class_="article-metaline-right")
for d in ds:
    d.extract()
ds = content.find_all("div", class_="push")
for d in ds:
    d.extract()
print("內文:", content.text)
saved["content"] = content.text

# 儲存內文(JSON)
f = open(dn + "/meta.json", "w", encoding="utf-8")
json.dump(saved, f)
f.close()