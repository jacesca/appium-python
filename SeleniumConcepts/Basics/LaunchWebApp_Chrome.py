"""
Run
python -m SeleniumConcepts.Basics.LaunchWebApp_Chrome
"""
import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('http://dummypoint.com/seleniumtemplate.html')

time.sleep(5)
driver.quit()
