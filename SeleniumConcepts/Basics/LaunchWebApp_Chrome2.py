"""
Run
python -m SeleniumConcepts.Basics.LaunchWebApp_Chrome2
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service = Service(executable_path='/opt/homebrew/bin/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options, service=service)
driver.get('http://dummypoint.com/seleniumtemplate.html')

time.sleep(5)
driver.quit()
