import requests
from bs4 import BeautifulSoup
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
print(soup.find('div'))
price = (soup.find("h4",{"class":"pull-right price"}))
print(price)
desc = (soup.find("p",{"class":"description"}))
print(desc.string)
                  # __or__
a = (soup.find("p",class_ = "description"))
print(a.string)