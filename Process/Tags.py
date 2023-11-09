import requests
from bs4 import BeautifulSoup
url = "https://webscraper.io/test-site/e-commerce/allinone/computers"
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")
print(soup.div)
print(soup.div.a) # For getting "a" tags
print(soup.div.ul) # For getting "ul" tags

