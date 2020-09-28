import requests
import time
import json

for i in range(1000000):
    url = f"https://www.myhome.ge/en/s/?Keyword=Tbilisi&AdTypeID=1&PrTypeID=1&Page={i}&mapC=41.73188%2C44.83688&mapZ=12&mapOp=0&EnableMap=0&cities=1996871&GID=1996871&Ajax=1"

    payload = {}
    headers = {
    'Cookie': 'ka=da; RENDER_MOBILE=A; Lang=en; PHPSESSID=tor5ep2tnknup4quqkubim6pb2'
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    page = response.json()
    with open(f"data-{i}.json", "w") as f:
        json.dump(page, f, indent=4)
    print(i, page["StatusCode"])
    time.sleep(1)