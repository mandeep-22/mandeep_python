



from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

driver=webdriver.Chrome("C:\pydev_chrome\chromedriver.exe")
driver.get("")
driver.find_element_by_name().send_keys()
driver.find_element_by_id(_).send_keys()
driver.find_element_by_xpath("//input[@value='Male']").click()
driver.find_element_by_name("UserName").send_keys("mandy")
driver.find_element_by_name("firstName").send_keys("john")
driver.find_element_by_id("lastName").send_keys("doe")
driver.find_element_by_xpath("//input[@value='Male']").click()
driver.find_element_by_xpath("//input[@value='Female']").click()

    
 


select = select(driver.find_element_by_name(""))
select.select_by