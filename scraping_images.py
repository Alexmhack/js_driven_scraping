from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Firefox()
url = "https://amazon.com"

amazon = driver.get(url)
html = driver.execute_script("return document.documentElement.outerHTML")

soup = BeautifulSoup(html)

images = []
for img in soup.findAll('img'):
	src = img.get("src")
	images.append(src)

print(images)
