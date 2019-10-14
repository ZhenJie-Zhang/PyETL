# [MAC]: SSL Ceritificate Fail
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from urllib.request import urlopen, urlretrieve
import json
import os

url = "https://www.google.com/doodles/json/2019/8?hl=zh_TW"
# 這個回應比較像是開啟一個遠端的檔案這樣的感覺
response = urlopen(url)
# load: 檔案 -> Dict/List
# loads: 字串 -> Dict/List
pics = json.load(response)
# pics: List p: Dict
for p in pics:
    print(p["title"])
    purl = "https:" + p["url"]
    print(purl)

    # urlretrieve("下載網址", "下載後的檔名")
    dn = "pictures"
    fn =  dn + "/" + purl.split("/")[-1]
    # 創資料夾, 要不存在才能創
    if not os.path.exists(dn):
        os.makedirs(dn)
    urlretrieve(purl, fn)