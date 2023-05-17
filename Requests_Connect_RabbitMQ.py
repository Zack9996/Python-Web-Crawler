import requests
from bs4 import BeautifulSoup
import os

url = "http://192.168.70.124:22988/#/"
response = requests.get(url)
print(response.text)


def createHTML():
    directory_name = "html"
    if os.path.exists(directory_name):
        print("目錄建立成功！")
    else:
        os.mkdir(directory_name)
        print("目錄建立失敗！")
    index = open("./html/index.html", "w")
    index.write(response.text)
    index.close()  # 確保檔案資源得到正確的釋放，同時也可以避免資源浪費和資料丟失的問題。


def postTest():
    url = "http://192.168.70.124:22988/#/"
    data = {"username": "guest", "password": "guest"}
    response = requests.post(url, data=data, allow_redirects=True)
    print(response.text)
    if  response.history:
        print("Request was redirected")
        for resp in response.history:
            print(resp.status_code, resp.url)
        print("Final destination:")
        print(response.status_code, response.url)
    else:
        print("Request was not redirected")


# createHTML()
# postTest()