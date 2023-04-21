from selenium import webdriver  # 導入webdriver，讓我們對瀏覽器溝通。

from selenium.webdriver.common.by import By  # 在 Selenium 中，By 是一個類別，它包含了多種元素定位方式，例如 ID、Name、Class Name、CSS Selector、XPath
from selenium.webdriver.support.ui import WebDriverWait # 我們可以指定一個最長等待時間，然後在這段時間內不斷地查找元素，直到元素出現為止。
from selenium.webdriver.support import expected_conditions as EC# 包含了多種等待條件，例如元素是否可見、元素是否存在、元素是否可點擊
from selenium.webdriver.common.keys import Keys  # 導入鍵盤模組，通過 Keys 類別，我們可以模擬鍵盤操作

import time  # 導入標準庫中的時間模組（time module），這個模組提供了與時間有關的函數和方法。
import os  # os 模組可以讓你建立、讀取、寫入檔案，刪除檔案或目錄
import wget  # 這個模組使用前需要確認是否有安裝過，請使用pip list查看。若要安裝請輸入指令：pip install wget

# wget 用於從網絡上下載文件，支持 HTTP、HTTPS 和 FTP 等多種協議。
import mysql.connector  # 導入連線mysql的模組

# options = webdriver.ChromeOptions()
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")

# driver = webdriver.Chrome(options=options)

# ------ 下面為webdriver執行檔位置、檔案本體 ------
PATH = "C:/Users/zackhuang/Desktop/chromedriver_win32.exe"  # 這是webdriver程序檔案的路徑。
driver = webdriver.Chrome(PATH)  # 透過webdriver打開瀏覽器
# ------ The End下面為webdriver執行檔位置、檔案本體 ------


def PTT():  # 如目前到問題是如果進入到沒有link的標籤則爬蟲會中斷
    driver.get("https://www.ptt.cc/bbs/Stock/index.html")  # 取得PTT 股票版網址並進入
    print("------ 進入PTT股票版 ------")

    def viewPost():
        titles = driver.find_elements(By.CLASS_NAME, "title")  # 取得所有文章的title
        titleLength = len(titles)
        for i in range(titleLength):  # 走訪文章
            # print("即將要進入的文章是：" + title.text) # 打印出目前要進入的文章標題
            title = titles[i].text
            titleHeader = titles[i].text[0]
            if titleHeader == "(":  # 這個標籤開頭代表文章已被刪除
                print("這邊文章被刪除了")
                # time.sleep(10)
            else:
                print("即將要進入的文章是：" + title)  # 打印出目前要進入的文章標題
                link = driver.find_element(By.LINK_TEXT, title)  # 取得有連結的文章標題
                link.click()  # 點擊文章標題
                # ------ 下方進入文章 ------
                WebDriverWait(driver, 10).until(  # 出現返回看板按鈕的時候返回上一頁
                    EC.presence_of_element_located((By.CLASS_NAME, "board"))
                )
                print("進入文章了")
                driver.back()  # 回到上一頁
                WebDriverWait(driver, 10).until(  # 出現看板的時候繼續迴圈
                    EC.presence_of_element_located((By.CLASS_NAME, "action-bar"))
                )
        olderPage = driver.find_element(By.LINK_TEXT, "‹ 上頁")  # 走訪這一頁所有文章後回到上一頁繼續走訪
        olderPage.click()  # 點擊上一頁
        time.sleep(1)
        print("這一頁跑完了!")
        viewPost()  # 在新的頁面後重新走訪

    viewPost()  # 開始走訪文章


def Dcard():
    driver.get("https://www.dcard.tw/f")  # Dcard
    time.sleep(1)  # 載入網頁需要一點時間，所以這裡需要延遲一下
    search = driver.find_element(By.NAME, "query")  # 選取搜尋欄位
    search.clear()  # 清除搜尋欄位，因為有時候搜尋欄位會有預設的內容。
    search.send_keys("星宇航空")  # 在搜尋欄位輸入星宇航空
    time.sleep(1)  # 輸入文字需要一點時間，所以這裡需要延遲一下
    search.send_keys(Keys.RETURN)  # 在搜尋欄位按下鍵盤的Enter鍵。
    time.sleep(10)  #
    print("done!")  # 執行結束


def testPTT():
    driver.get("https://www.ptt.cc/bbs/Stock/index.html")
    print("------ 進入PTT股票版 ------")

    def getTitles():
        titles = driver.find_elements(By.CLASS_NAME, "title")
        title_lenth = len(driver.find_elements(By.CLASS_NAME, "title"))
        # print(title_lenth) 文章數量

        mydb = mysql.connector.connect(
            host="localhost", user="root", password="root", database="python"
        )
        cursor = mydb.cursor()
        for i in range(title_lenth):
            if titles[i].text[0] != "(":
                cursor.execute(
                    "INSERT INTO `data`(`ppt_post_title`) VALUES ('"
                    + titles[i].text
                    + "');"
                )
                print(titles[i].text)
            else:
                print("這個被刪除了")

        olderPage = WebDriverWait(driver, 10).until(  # 走訪這一頁的所有文章後，回到上一頁繼續走訪。
            EC.presence_of_element_located((By.LINK_TEXT, "‹ 上頁"))
        )
        olderPage.click()  # 點擊上一頁
        print("------ 這一頁跑完了! ------")
        cursor.close()
        mydb.commit()
        mydb.close()  # 關閉資料庫連線
        getTitles()  # 在新的頁面後重新走訪

    getTitles()


def eney():
    driver.get("http://www.eyny.com/index.php")
    print(print("------ 進入伊利討論區首頁 ------"))

    def stock():
        goLink = WebDriverWait(driver, 3).until(  # 走訪這一頁的所有文章後，回到上一頁繼續走訪。
            EC.presence_of_element_located((By.LINK_TEXT, "股票討論"))
        )
        goLink.click()
        print(print("------ 進入伊利討論區股票討論 ------"))
        WebDriverWait(driver, 3).until(  # 走訪這一頁的所有文章後，回到上一頁繼續走訪。
            EC.presence_of_element_located((By.CLASS_NAME, "p_pre"))
        )
        imgs = driver.find_elements(By.CLASS_NAME, "p_pre")
        photoName = "stock_images"
        path = os.path.join(photoName)
        if os.path.exists(photoName):
            print("圖片資料夾已存在。")
        else:
            os.mkdir(path)  # 依據這個路徑創建資料夾
            print("建立圖片資料夾。")
        count = 1
        for img in imgs:
            savePath = os.path.join(path, photoName + str(count) + ".jpg")  # 圖片下載位置
            # print(img.get_attribute("src")) # 取得img這個元素的屬性。
            wget.download(img.get_attribute("src"), savePath)  # 取得圖片url位置並下載至指定路徑。
            count += 1
        time.sleep(10)

    stock()


def stock():
    driver.get("https://www.cnyes.com/usstock")
    print("------ " + driver.title + " ------")

    def search():
        search = driver.find_element(
            By.XPATH,
            '//*[@id="anue-ga-wrapper"]/div[1]/div[1]/div/nav/header/div[2]/div/div[1]/div/input',
        )
        search.send_keys("美國10年公債殖利率")
        time.sleep(1)
        search.send_keys(Keys.RETURN)
        time.sleep(1)
        products = driver.find_elements(By.CLASS_NAME, "row")
        productsCategory = driver.find_elements(By.CLASS_NAME, "row_cat")
        stocksCode = driver.find_elements(By.CLASS_NAME, "info_code")
        stocksTitle = driver.find_elements(By.CLASS_NAME, "info_title")
        for i in range(len(products)):
            print("股票代碼：" + stocksCode[i].text)
            print("股票中文名稱：" + stocksTitle[i].text)
            print(productsCategory[i].text)
            productCategory = productsCategory[i].text
            products[i].click()
            if productCategory == "基金":
                stockPrice = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//div[@class="_1SFOH _1c2Sw"]')
                    )
                )
                print("目前單位淨值：" + stockPrice.text)
            elif productCategory == "商品期貨":
                result = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "info-lp"))
                )
                print("目前殖利率：" + result.text)
            print("------")
            driver.back()  # 回到上一頁
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "header_title"))
            )

    search()
    print("run done!")


# stock()
# driver.get("https://shopee.tw/")
# search = driver.find_element(By.CLASS_NAME,"shopee-searchbar-input__input")
# search.send_keys("衣服")
# search.send_keys(Keys.RETURN)
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME,'AF3TXt'))
# )
# print("666")
# time.sleep(0.5)
# imgs = driver.find_element(By.XPATH, '//div[@class="_8VOHhl aAd6P9"]')
# print(imgs.text)
# imgs.tag_name
# for img in imgs:
#     print(img.get_attribute("src"))
# time.sleep(5)
# Photos = driver.find_elements(By.XPATH,'//div[@class="_7DTxhh vc8g9F"]')
# # PhotoText = Photos.get_attribute("alt")
# for i in range(len(Photos)):
#     print(Photos[i].get_attribute("alt"))
# time.sleep(3)

# Dcard()
# PTT()
# testPTT()
# eney()
# driver.get("https://httpbin.org/user-agent")
# time.sleep(10)
