import requests

url = "https://api.flipsidecrypto.com/api/v2/metrics/projects?api_key=3e2f65bf-7613-41f8-8e76-be8b7565c707"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text.encode('utf8'))



import numpy as np
import pprint
import json

r = requests.get("https://api.flipsidecrypto.com/api/v2/metrics/projects?api_key=3e2f65bf-7613-41f8-8e76-be8b7565c707")
r.json()
#pprint.pprint(r.json())                                      #["posts"] - create a list of posts

#pprint.pprint(r.json()["posts"][0])                         #[0] - index of in posts
#pprint.pprint(r.json()["posts"][0]["url_for_post"])         #request only the url

r_text = r.text

data = json.loads(r_text)
print(data)
print(type(data))                       #dictionary

data_serialised = json.dumps(data)
print(type(data_serialised))            #string

data_serialised = json.dump(data, open('data.json', "w"), indent = 4)






