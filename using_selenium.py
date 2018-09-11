import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.google.com')

html = driver.execute_script("return document.documentElement.outerHTML")
py_soup = BeautifulSoup(html, 'html.parser')
