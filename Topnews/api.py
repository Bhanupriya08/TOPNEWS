import json
import requests

url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=f3ec9f1b577a447eb1bc756fd5570219')
response = requests.get(url).json()
content = json.dumps(response, indent = 4 )

data = json.loads(content)

news = []
abc = ["title","description","content","url","author"]
if data["status"] == "ok":
    for info in data["articles"]:
        l = []
        for key,value in info.items():
            if key in abc:
                l.append(value)
        news.append(l)
