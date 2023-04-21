from selenium import webdriver  # 導入webdriver，讓我們對瀏覽器溝通。
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless") # 加入--headless這個參數，開啟headless模式，
# --headless這個模式不會開啟google chrome這個瀏覽器，但仍會跑取網頁資料。
# ------ 下面為webdriver執行檔位置、檔案本體 ------
PATH = "C:/Users/zackhuang/Desktop/chromedriver_win32.exe"  # 這是webdriver程序檔案的路徑。
driver = webdriver.Chrome(PATH,options=options)  # 透過webdriver打開瀏覽器
# ------ The End下面為webdriver執行檔位置、檔案本體 ------
driver.implicitly_wait(10) # 網站Title隱含等待10秒鐘，以便等待瀏覽器成功載入HTML網頁，參數10秒是最長等待時間。
driver.get("https://togkf.tw/home") # 輸入網址並進入網站
print(driver.title) # 打印出網站tiele
html = driver.page_source # 網站內容
print(html)

