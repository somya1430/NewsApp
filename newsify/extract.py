import requests
import json

# Enter url of any site
url = "<url>"
data = requests.get(url)
print(data)
content = data.content
print(content)
