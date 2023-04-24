import requests
from bs4 import BeautifulSoup
url = "https://zackspiecewebsite.netlify.app"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text,"lxml")
    # tags = soup("a")
    # for tag in tags:
    #     print(tag.get("href",None))
else:
    print("error,HTTP request failed......")