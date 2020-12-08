import requests
import json

url = 'http://0.0.0.0:5000/predict/'

data = [[43415, 658, 23878.25, 180, 0.036, 3, 179930, 71972, 31.84568, -102.36764, 94700, 44174]]
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)