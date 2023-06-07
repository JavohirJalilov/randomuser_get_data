import requests
import json

p = {
    "results": 5,
    "gender": "female"
}
url = 'https://randomuser.me/api/'

r = requests.get(url, params=p)

print(r.url)