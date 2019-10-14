from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
url = "https://www.ptt.cc/bbs/Beauty/M.1566650688.A.F81.html"
r = Request(url)
r.add_header("user-agent", "Mozilla/5.0")
response = urlopen(r)
html = BeautifulSoup(response)
print(html)