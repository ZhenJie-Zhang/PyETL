import requests
from bs4 import BeautifulSoup

start = 3037
howmany = 5
total = []
for i in range(howmany):
    url = "https://www.ptt.cc/bbs/Beauty/index" + str(start - i) + ".html"
    response = requests.get(url, cookies={"over18":"1"})
    html = BeautifulSoup(response.text)
    for t in html.find_all("div", class_="title"):
        # 沒有a代表被刪除
        if not t.find("a") == None:
            turl = "https://www.ptt.cc" + t.find("a")["href"]
            total.append(turl)
print(total)
