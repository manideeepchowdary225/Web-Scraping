import requests
url = "https://www.amazon.in/"
r = requests.get(url)
print(r.status_code)
print(r.text)
