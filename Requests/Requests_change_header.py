import requests

# url = "https://www.momoshop.com.tw/main/Main.jsp"
url = "https://licenseexam.vaserver.com/"
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    ' AppleWebKit/537.36 (KHTML, like Gecko)'
    ' Chrome/112.0.0.0 Safari/537.36'
}
r = requests.get(url,headers=headers)
if r.status_code == requests.codes.ok:
    print(r.text)
else:
    print("http請求錯誤...",url)
