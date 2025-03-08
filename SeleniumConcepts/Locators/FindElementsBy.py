"""
Run
python -m SeleniumConcepts.Locators.FindElementsBy
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('http://dummypoint.com/Form.html')
time.sleep(2)

# Locators
elements = driver.find_elements(By.ID, "g")
for elem in elements:
    print(elem.get_attribute('value'), elem.is_selected())

time.sleep(5)
driver.quit()
