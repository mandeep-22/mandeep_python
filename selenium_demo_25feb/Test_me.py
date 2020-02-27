'''
Created on Feb 27, 2020

@author: training_d5.01.02
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome("C:\pydev_chrome\chromedriver.exe")
driver.get("https://lkmdemoaut.accenture.com/TestMeApp/fetchcat.htm")

driver.maximize_window()

window_b = driver.window_handles[0]
about_us = driver.find_element_by_link_text("AboutUs")
our_office = driver.find_element_by_xpath("//*[@id='menu3']/li[3]/ul/li/a/span")
chennailocation = driver.find_element_by_xpath("//*[@id='menu3']/li[3]/ul/li/ul/li[1]/a/span")

action1 = ActionChains(driver)
action1.move_to_element(about_us).move_to_element(our_office).move_to_element( chennailocation).click( chennailocation).perform()
window_a = driver.window_handles[1]

driver.switch_to.window(window_a)
driver.switch_to.frame("main_page")
txt = driver.find_element_by_id("demo3").text
print(txt)
driver.quit()




