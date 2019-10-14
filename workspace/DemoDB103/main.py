# https://repl.it/@Elwing/0826demo
# https://0826demo.elwing.repl.run
# [MAC]:SSL Ceritificte Fail
from urllib.request import urlopen, urlretrieve
import json
import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


for y in range(2018, 2020):
    # range(12) -> 0~11
    for m in range(12):
        url = "https://www.google.com/doodles/json/" + str(y) + "/" + str(m + 1) + "?hl=zh_TW"
        print(url)
        # 這個回應比較像是開啟一個遠端的檔案這樣的感覺
        response = urlopen(url)
        # json.load(file_path)
        # load: 檔案 -> Dict/List
        # loads: 字串 -> Dict/List
        pics = json.load(response)
        # pics: List p:Dict
        for p in pics:
            print(p["title"])
            purl = "https:" + p["url"]
            print(purl)

            # urlretrieve("下載網址", "下載後檔名")
            dn = "pictures/" + str(y) + "/" + str(m + 1)
            fn = dn + "/" + purl.split("/")[-1]
            # 創資料夾，要不存在才能創
            # path: a/b/c/d
            # os.mkdir(path, mode) -> 只建立最後一個資料夾"d"
            # os.makedirs(path, mode, exist_ok) -> 建立a/b/c/d所有的資料夾
            if not os.path.exists(dn):
                os.makedirs(dn)
            urlretrieve(purl, fn)
