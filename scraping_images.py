from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Firefox()
url = "https://amazon.com"

amazon = driver.get(url)
html = driver.execute_script("return document.documentElement.outerHTML")

soup = BeautifulSoup(html)

images = soup.findAll('img')
print(len(images))

for img in images:
	print(img.get("src"))
