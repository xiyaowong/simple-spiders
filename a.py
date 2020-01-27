import requests
import json

payload = {
    't': 'bilibili_cover',
    'url': 'https://www.bilibili.com/video/av78977736'
}

headers = {
    'Content-Type':'application/json'
}
rep = requests.post('http://localhost:5000/author=wongxy', data=json.dumps(payload), headers =headers)
print(rep.status_code)
print(rep.json())