import requests
from bs4 import BeautifulSoup

url = "https://www.chrisburkard.com/Shop/Best-Sellers/"

web_r = requests.get(url)
web_soup = BeautifulSoup(web_r.text, 'html.parser')

print(web_soup.findAll('img'))
