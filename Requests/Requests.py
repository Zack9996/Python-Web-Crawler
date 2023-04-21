import requests

# url = "https://zackspiecewebsite.netlify.app/"
# url = "https://www.dcard.tw/f"

# ------以下簡單測試requests------
url = "https://togkf.tw/home" # 網站網址
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}
# r = requests.get(url, headers=headers)
response = requests.get(url, headers=headers) # 訪入網站
print(response.status_code)
if response.status_code == 200:
    print(response.text) # 取得網站的結構、內容
    print("編碼:", response.encoding) # 取的網站的編碼方式
else:
    print("error,HTTP request failed......")
# ------The End 以下簡單測試requests------

# post_data = {"name":"zack","grade":22} # HTML 表單欄位資料
# r = requests.post("https://httpbin.org/post",post_data) # 送出HTTP request，參數是送出的資料
# print(r.text)

# ------使用params參數------
# url = "https://httpbin.org/get"
# url_params = {"a":15,"b":22}
# r = requests.get(url,params=url_params)
# if r.status_code == 200:
#     print(r.text)
# else:
#     print("error,HTTP request failed......")
# ------The End使用params參數------


# ------自訂Header user-agent方法------
# url = "https://httpbin.org/user-agent"
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
# }
# r = requests.get(url, headers=headers)
# if r.status_code == 200:
#     print(r.text)
# else:
#     print("error,HTTP request failed......")
# ------The End自訂Header user-agent方法------

# ------加入cookie資料方法------
# url = "https://httpbin.org/cookies"
# cookies = dict(name='Zack Huang')
# r =requests.get(url,cookies=cookies)
# print(r.text)
# ------The End加入cookie資料方法------