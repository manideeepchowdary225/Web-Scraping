import requests
from bs4 import BeautifulSoup
import re
url = "https://webscraper.io/test-site/e-commerce/allinone/computers/tablets"
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")
 # data = soup.find_all(string = "Galaxy tab") # Passing single frame
data = soup.find_all(string = re.compile("Galaxy")) # We can change the tab with anything in place of galaxy
print(data)

