"""
Run
python -m SeleniumConcepts.Basics.LaunchWebApp_Firefox
"""
import time
from selenium import webdriver


driver = webdriver.Firefox()
driver.get('http://dummypoint.com/seleniumtemplate.html')

time.sleep(5)
driver.quit()
