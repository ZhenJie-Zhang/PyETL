from selenium.webdriver import Chrome
import time

driver = Chrome("./chromedriver")
driver.get("https://www.youtube.com/view_all_playlists")

driver.find_element_by_id("identifierId")\
      .send_keys("abc1233108@gmail.com")

driver.find_element_by_id("identifierNext").click()

time.sleep(3)
# 輸入密碼
driver.find_element_by_class_name("whsOnd")\
      .send_keys("654321aA")
# xxrfaxmvvbusqyfq
driver.find_element_by_id("passwordNext").click()

time.sleep(5)
driver.find_element_by_id("identity-prompt-confirm-button").click()
playlists = driver.find_element_by_id("vm-video-title-text")
for p in playlists:
    print(p.text)