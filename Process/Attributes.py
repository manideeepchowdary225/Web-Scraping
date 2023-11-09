import requests
from bs4 import BeautifulSoup
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
tag = soup.header
atb = (tag.attrs)
print(atb["role"])