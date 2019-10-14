from selenium.webdriver import Chrome
import time

driver = Chrome("./chromedriver")
# 跟你平常操作一模一樣
driver.get("https://www.facebook.com")
# find: find_element!!!!
# find_all: find_elements!!!!
driver.find_element_by_id("email").send_keys("abc1233108@yahoo.com.tw")
driver.find_element_by_id("pass").send_keys("Dfgh-0147")
driver.find_element_by_id("loginbutton").click()

c = input("請輸入驗證碼:")
driver.find_element_by_id("approvals_code").send_keys(c)
time.sleep(1)
driver.find_element_by_id("checkpointSubmitButton").click()

time.sleep(3)
driver.find_element_by_id("checkpointSubmitButton").click()
content = driver.find_element_by_class_name("userContent")

print("第一則貼文內容", content.text)
time.sleep(3)
driver.close()