# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 10:33:29 2020

@author: rmbp
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


# Setting up the driver and environment 
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


# Examplewebsite
driver.get("https://techwithtim.net")
print(driver.title)


# Search bar and locating elements through HTML
search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)


#print(driver.page_source)

# Wait until presence of element is made

try:
    main = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"main"))
        )
    
    articles = main.find_element_by_tag_name("article")
    for article in articles:
        header = article.find_elements_by_class_name("a")[0]
        print(header.text)

finally:
    driver.quit()



#time.sleep(5)

