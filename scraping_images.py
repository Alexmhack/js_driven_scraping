import os
import requests
import shutil
import time

from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Firefox()
url = "https://amazon.com"

amazon = driver.get(url)
count = 0

while count < 10:
    html = driver.execute_script("return document.documentElement.outerHTML")
    soup = BeautifulSoup(html, 'html.parser')
    images = []
    for img in soup.findAll('img')[10]:
        src = img.get("src")
        images.append(src)

    current_path = os.getcwd()
    for img in images:
        try:
            file_path = os.path.basename(img)
            img_res = requests.get(img, stream=True)
            new_path = os.path.join(current_path, 'images', file_path)

            with open(new_path, 'wb') as output_file:
                shutil.copyfileobj(img_res.raw, output_file)

            del img_res
        except Exception as e:
            print(e)
            pass

    count += 1
    time.sleep(5)
