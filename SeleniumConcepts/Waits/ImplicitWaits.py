"""
Run
python -m SeleniumConcepts.Waits.ImplicitWaits
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('http://dummypoint.com/seleniumtemplate.html')
driver.implicitly_wait(10)
time.sleep(2)

driver.find_element(By.ID, "user_input").send_keys('Code2Lead')

time.sleep(5)
driver.quit()
