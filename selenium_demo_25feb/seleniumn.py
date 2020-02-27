'''
Created on Feb 26, 2020

@author: training_d5.01.02
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome("C:\pydev_chrome\chromedriver.exe")
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
driver.maximize_window()
sub = driver.find_element_by_id("sub-menu")

action = ActionChains(driver)

action.move_to_element(sub).perform()
 
google_link = driver.find_element_by_id("link2")
action = ActionChains(driver)
action.move_to_element(sub).move_to_element(google_link).click(google_link).perform()
driver.back()
action1 = ActionChains(driver)
double_click = driver.find_element_by_id("double-click")
action1.double_click(double_click).perform()
alert = driver.switch_to_alert()
abc = alert.text
print(abc)
alert.accept()

