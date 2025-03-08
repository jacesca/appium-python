"""
Run
python -m SeleniumConcepts.Basics.LaunchWebApp_Safari
"""
import time
from selenium import webdriver


driver = webdriver.Safari()
driver.get('http://dummypoint.com/seleniumtemplate.html')

time.sleep(5)
driver.quit()
