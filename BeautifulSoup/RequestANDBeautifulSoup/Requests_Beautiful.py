import requests
from bs4 import BeautifulSoup

def firstTest():
    url = "https://zackspiecewebsite.netlify.app"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text,"lxml")
        tags = soup('a')
        for tag in tags:
            print(tag.text)
            # print(tag["href"])
            # print(tag.get("href", None))
            print(tag.attrs)
            print("------")
    else:
        print("error,HTTP request failed......")

def selectOne():
    url = "https://zackspiecewebsite.netlify.app"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text,"lxml")
        tag = soup.select_one(".top")
        print(tag.select_one("h1"))
        print(tag.artts)
    else:
        print("error,HTTP request failed......")

# firstTest()
# selectOne()