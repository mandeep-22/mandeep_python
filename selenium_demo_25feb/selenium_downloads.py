'''
Created on Feb 26, 2020

@author: training_d5.01.02
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome("C:\pydev_chrome\chromedriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")
driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("com.thoughtworks.selenium").click()
driver.switch_to.default_content()
driver.switch_to.frame(1)
driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("com.thoughtworks.selenium").click()
time.sleep(2)
driver.switch_to.default_content()
driver.switch_to.frame(2)


