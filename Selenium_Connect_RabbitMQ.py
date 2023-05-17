from selenium import webdriver  # 導入webdriver，讓我們對瀏覽器溝通。

from selenium.webdriver.common.by import By  # 在 Selenium 中，By 是一個類別，它包含了多種元素定位方式，例如 ID、Name、Class Name、CSS Selector、XPath
from selenium.webdriver.support.ui import WebDriverWait # 我們可以指定一個最長等待時間，然後在這段時間內不斷地查找元素，直到元素出現為止。
from selenium.webdriver.support import expected_conditions as EC# 包含了多種等待條件，例如元素是否可見、元素是否存在、元素是否可點擊
from selenium.webdriver.common.keys import Keys  # 導入鍵盤模組，通過 Keys 類別，我們可以模擬鍵盤操作

import time  # 導入標準庫中的時間模組（time module），這個模組提供了與時間有關的函數和方法。

import requests

# ------ 下面為webdriver執行檔位置、檔案本體 ------
PATH = "C:/Users/zackhuang/Desktop/chromedriver_win32.exe"  # 這是webdriver程序檔案的路徑。
driver = webdriver.Chrome(PATH)  # 透過webdriver打開瀏覽器
# ------ The End下面為webdriver執行檔位置、檔案本體 ------
driver.get("http://192.168.70.124:22988/")
print(driver.page_source)
username = driver.find_element(By.NAME,"username")
password =driver.find_element(By.NAME,"password")
submit = driver.find_element(By.CSS_SELECTOR,"input[type='submit']")
username.send_keys("guest")
password.send_keys("guest")
time.sleep(1)
submit.click()

# 获取当前页面的URL
# current_url = driver.current_url
# 打印当前页面的URL
# print(current_url)

time.sleep(1)
print(driver.page_source)
aTags = driver.find_elements(By.TAG_NAME,"a")
cssTags = driver.find_elements(By.TAG_NAME,"link")
jsTags = driver.find_elements(By.TAG_NAME,"script")
time.sleep(1)



for i in range(len(aTags)):
    # time.sleep(2)
    # url = aTags[i].get_attribute("href")
    # driver.get(url)
    # time.sleep(2)
    # print(driver.page_source)
    # time.sleep(2)

    url = aTags[i].get_attribute("href")
    r = requests.get(url)
    print(r.text)
    print("--------",i,"-----------")
print(len(aTags))
# for css in cssTags:
#     time.sleep(1)
#     driver.get(css.get_attribute("href"))
#     time.sleep(1)
#     print(driver.page_source)
#     time.sleep(1)

# for js in jsTags:
#     time.sleep(1)
#     driver.get(js.get_attribute("href"))
#     time.sleep(1)
#     print(driver.page_source)
#     time.sleep(1)
print("----------The end.---------")
# driver.get("https://www.GOOGLE.com")
# time.sleep(3)
# driver.get("https://www.youtube.com")
# time.sleep(5)