import requests
from bs4 import BeautifulSoup
import schedule
import time
from twilio.rest import Client

def job():
    url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
    response = requests.get(url)
    html = BeautifulSoup(response.text)
    rows = html.find("table").find("tbody").find_all("tr")
    for r in rows:
        tds = r.find_all("td")
        if "日圓" in tds[0].text:
            print("日圓匯率:", tds[2].text)
            account_sid = 'twilio帳號'
            auth_token = 'twilio密碼'
            client = Client(account_sid, auth_token)

            client.messages.create(
                body="日圓匯率:" + tds[2].text,
                from_='twilio電話',
                to='寄送簡訊對象+8869...')


schedule.every().day.at("19:29").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)




# import requests
# from bs4 import BeautifulSoup
# import schedule
# import time
# from twilio.rest import Client
#
# def job():
#     url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
#     response = requests.get(url)
#     html = BeautifulSoup(response.text)
#     rows = html.find("table").find("tbody").find_all("tr")
#     for r in rows:
#         tds = r.find_all("td")
#         if "日圓" in tds[0].text:
#             print("日圓匯率:", tds[2].text)
#             account_sid = 'AC57cfa7b7972aa7e166a10f1cd1352866'
#             auth_token = '6fdb0942ae72e39b34ef3c512a4e53dd'
#             client = Client(account_sid, auth_token)
#
#             client.messages.create(
#                 body="日圓匯率:" + tds[2].text,
#                 from_='',
#                 to='')
#
#
# schedule.every().day.at("19:29").do(job)
# while True:
#     schedule.run_pending()
#     time.sleep(1)