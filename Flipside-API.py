import requests

url = "https://api.flipsidecrypto.com/api/v2/metrics/projects?api_key=3e2f65bf-7613-41f8-8e76-be8b7565c707"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text.encode('utf8'))



import numpy as np
import pprint


r = requests.get("https://api.flipsidecrypto.com/api/v2/metrics/projects?api_key=3e2f65bf-7613-41f8-8e76-be8b7565c707")
r.json()
pprint.pprint(r.json())                                      #["posts"] - create a list of posts
#pprint.pprint(r.json()["posts"][0])                         #[0] - index of in posts
#pprint.pprint(r.json()["posts"][0]["url_for_post"])         #request only the url



#RESULT
#[{'cmc_id': 2569,
#          'id': '0031aea9-2b0d-4052-9a80-4efd28271e45',
#          'name': 'CoinPoker',
#          'short_name': 'CoinPoker',
#          'slug': '',
#          'symbol': 'CHP'},

