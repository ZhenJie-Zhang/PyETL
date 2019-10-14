import requests
import os
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore')


# url = "https://www.ptt.cc/bbs/Beauty/M.1566650688.A.F81.html"
url = "https://www.ptt.cc/bbs/Beauty/M.1566707650.A.E8C.html"
# url = "https://www.ptt.cc/bbs/Beauty/M.1565546636.A.1D0.html"

response = requests.get(url, cookies={"over18": "1"}).text
# 如果是requests，多一個步驟，.text欄位拿出
html = BeautifulSoup(response)

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
