import requests
from bs4 import BeautifulSoup
url = "https://webscraper.io/test-site/e-commerce/allinone/computers"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
price = soup.find_all("h4", class_ = "pull-right price")
print(len(price))
for i in price:
    print(i.text)
print(price[3]) # This gives a particular 4th box price
desc = soup.find_all("p", class_ = "description")
print(desc[3]) # Same for description