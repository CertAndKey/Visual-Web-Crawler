#!/usr/bin/env python
#
#
#THIS SCRIPT CRAWLS THROUGH WEB PAGE ENDPOINTS
#THIS SCRIPT TAKES ONE ARGUMENT, WHICH IS A TEXT FILE OF ENDPOINTS
#
#
import sys
import time
import signal
import json
from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from webdriver_manager.chrome import ChromeDriverManager



#check inputs

#proxy setup

#chrome browser setup
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")


#create driver object

driver = webdriver.Chrome(ChromeDriverManager().install())


#open URL

filepath = sys.argv[1]
with open(filepath) as fp:
   line = fp.readline()
   while line:
       print(line)
       driver.get('http://<ip_address>/' + line)
       line = fp.readline()
       time.sleep(1)




driver.close()
driver.quit()
