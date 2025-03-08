"""
Run
python -m SeleniumConcepts.Basics.LaunchWebApp_Safari2
"""
import time
from selenium import webdriver
from selenium.webdriver.safari.service import Service


service = Service(executable_path='/System/Cryptexes/App/usr/bin/safaridriver')
options = webdriver.SafariOptions()
driver = webdriver.Chrome(options=options, service=service)
driver.get('http://dummypoint.com/seleniumtemplate.html')

time.sleep(5)
driver.quit()
