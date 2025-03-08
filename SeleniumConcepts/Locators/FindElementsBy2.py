"""
Run
python -m SeleniumConcepts.Locators.FindElementsBy2
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('http://dummypoint.com/seleniumtemplate.html')
time.sleep(2)

# Locators
elements = driver.find_elements(By.CLASS_NAME, "breadcrumb-item")
for elem in elements:
    print(elem.text)

time.sleep(5)
driver.quit()
