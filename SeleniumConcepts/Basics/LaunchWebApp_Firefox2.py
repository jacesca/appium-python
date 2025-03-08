"""
Run
python -m SeleniumConcepts.Basics.LaunchWebApp_Firefox2
"""
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


service = Service(executable_path='/opt/homebrew/bin/geckodriver')
options = webdriver.FirefoxOptions()
driver = webdriver.Chrome(options=options, service=service)
driver.get('http://dummypoint.com/seleniumtemplate.html')

time.sleep(5)
driver.quit()
