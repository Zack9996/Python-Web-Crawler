import requests
import json
url = "https://index.ndc.gov.tw/n/json/lightscore"
jsonfile = "line.json"
r = requests.post(url)
r.encoding = "utf8"

json_data = json.loads(r.text)
print(json_data)



