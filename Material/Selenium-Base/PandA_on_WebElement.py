from selenium import webdriver
import time

from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec

driver = webdriver.Chrome("/Users/sujithreddy/Documents/Code2Lead/drivers/chromedriver")

driver.get("http://www.dummypoint.com/seleniumtemplate.html")
time.sleep(2)

wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])
ele = wait.until(ec.presence_of_element_located((By.ID,"user_input")))

#ele = driver.find_element(By.ID,"user_input")

ele_d = ele.is_displayed()
print("Is Displayed : ",ele_d)

ele_e = ele.is_enabled()
print("is enabled : ",ele_e)

ele_s = ele.size
print("Size of ele :" , ele_s)

ele_l = ele.location
print("Ele location : ",ele_l)

ele.click()

ele.send_keys("Code2Lead")
time.sleep(2)

ele.clear()
time.sleep(2)

ele.send_keys("Code2Lead_second time")
time.sleep(2)

ele_t = ele.get_attribute("value")
print("Text from Edit box : ",ele_t)


time.sleep(5)
driver.quit()