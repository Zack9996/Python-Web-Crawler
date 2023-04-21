from selenium import webdriver  # 導入webdriver，讓我們對瀏覽器溝通。

from selenium.webdriver.common.by import By  # 在 Selenium 中，By 是一個類別，它包含了多種元素定位方式，例如 ID、Name、Class Name、CSS Selector、XPath
from selenium.webdriver.support.ui import WebDriverWait # 我們可以指定一個最長等待時間，然後在這段時間內不斷地查找元素，直到元素出現為止。
from selenium.webdriver.support import expected_conditions as EC# 包含了多種等待條件，例如元素是否可見、元素是否存在、元素是否可點擊
from selenium.webdriver.common.keys import Keys  # 導入鍵盤模組，通過 Keys 類別，我們可以模擬鍵盤操作

import time  # 導入標準庫中的時間模組（time module），這個模組提供了與時間有關的函數和方法。

# ------ 下面為webdriver執行檔位置、檔案本體 ------
PATH = "C:/Users/zackhuang/Desktop/chromedriver_win32.exe"  # 這是webdriver程序檔案的路徑。
driver = webdriver.Chrome(PATH)  # 透過webdriver打開瀏覽器
# ------ The End下面為webdriver執行檔位置、檔案本體 ------
driver.implicitly_wait(10)
url="https://www.104.com.tw/jobs/main/student"
driver.get(url)


search = driver.find_element(By.NAME , "ikeyword")
search.send_keys("Python")
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)

allLinks = driver.find_elements(By.TAG_NAME,"link")
allScripts = driver.find_elements(By.TAG_NAME,"script")
allA = driver.find_elements(By.TAG_NAME,"a")
for link in allLinks:
    print("這是所有link標籤的連結："+link.get_attribute("href"))
print("------跑完所有link標籤了------")


for script in allScripts:
    print("這是所有script標籤的連結："+script.get_attribute("src"))
print("------跑完所有script標籤了------")

for a in allA:
    print("這是所有a標籤的連結："+a.get_attribute("href"))
print("------跑完所有a標籤了------")

time.sleep(1)
print("run done!")