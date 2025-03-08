"""
Run
python -m SeleniumConcepts.DriverMethods.DriverMethods
"""
import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('http://dummypoint.com/seleniumtemplate.html')
time.sleep(2)

# Title of page
assert "Selenium Template" in driver.title
time.sleep(2)

# Maximize Window
driver.maximize_window()
time.sleep(2)

# Minimize Window
driver.minimize_window()

time.sleep(5)
driver.quit()
