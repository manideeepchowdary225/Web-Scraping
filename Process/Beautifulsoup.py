import requests
from bs4 import BeautifulSoup
url = "https://webscraper.io/test-site/e-commerce/allinone/computers"
r = requests.get(url)
print(r.text)
soup = BeautifulSoup(r.text,"lxml")
print(soup)