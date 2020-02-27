'''
Created on Feb 26, 2020

@author: training_d5.01.02
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("C:\pydev_chrome\chromedriver.exe")
driver.get("https://netbanking.hdfcbank.com/netbanking/")
driver.switch_to.frame("login_page")
driver.find_element_by_name("fldLoginUserId").send_keys("77777")
driver.find_element_by_xpath("/html/body/form/table[2]/tbody/tr/td[2]/table/tbody/tr[1]/td[1]/table/tbody/tr[3]/td[2]/table/tbody/tr[6]/td[2]/a/img")
driver.switch_to.default_content()
driver.switch_to.frame("footer")
driver.find_element_by_xpath("").click()
driver.find_element_by_link_text("Privacy Policy").click()