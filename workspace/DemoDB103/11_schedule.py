import requests
from bs4 import BeautifulSoup
import schedule
import time
def job():
    url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
    response = requests.get(url)
    html = BeautifulSoup(response.text)
    rows = html.find("table").find("tbody").find_all("tr")
    for r in rows:
        tds = r.find_all("td")
        if "日圓" in tds[0].text:
            print("日圓匯率:", tds[2].text)


schedule.every(2).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)