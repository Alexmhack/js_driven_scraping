import os
import requests
import shutil

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

current_path = os.getcwd()

for img in images:
    try:
        file_path = os.path.basename(img)
        img_res = requests.get(img)
        new_path = os.path.join(current_path, 'images', file_path)

        with open(new_path, 'wb') as output_file:
            shutil.copyfileobj(img_res.raw, output_file)

        del img_res
    except Exception as e:
        print(e)
        pass
