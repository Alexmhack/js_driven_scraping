# js_driven_scraping
Scraping Javascript Driven Websites Using Python

Run ```js_scrape.py``` file and you should get lesser results of the images then 
actually exists on the website. This is due to the javascript getting loaded while
the website is also loading so python ```requests``` cannot scrape that for us

For scraping javascript-driven websites we need a more powerful python package
which is [selenium-python](https://selenium-python.readthedocs.io/)

Using the instructions given in the docs for selenium-python install the selenium 
and firefox drivers for selenium. Be sure to donwload 

![geckodriver](https://github.com/Alexmhack/js_driven_scraping/master/images/Capture.PNG)

Download ```32bit``` or ```64bit``` according to our specs for windows, unzip the 
folder and add the path of that folder in **system variables**

Create a new file named ```using_selenium.py``` 

```
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Firefox()
```

When you run the file the firefox browser with a new window should open. 

For opening a url in browser window, close the firefox browser and add 

```
driver.get('https://google.com')
```

at last. Then run the file again and the browser should open the google website
