'''
Created on Feb 26, 2020

@author: training_d5.01.02
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome("C:\pydev_chrome\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_name("Submit").click()
admin = driver.find_element_by_id("menu_admin_viewAdminModule")
usermanagement = driver.find_element_by_id("menu_admin_UserManagement")
user =  driver.find_element_by_id("menu_admin_viewSystemUsers")
action = ActionChains(driver)
action.move_to_element( admin).move_to_element( usermanagement).move_to_element(user).click(user).perform()
