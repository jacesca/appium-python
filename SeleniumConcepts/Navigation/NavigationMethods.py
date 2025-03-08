"""
Run
python -m SeleniumConcepts.Navigation.NavigationMethods
"""
import time
from selenium import webdriver


driver = webdriver.Chrome()

# Navigation actions
driver.get('http://dummypoint.com/seleniumtemplate.html')
time.sleep(2)

driver.get('https://www.google.com')
time.sleep(2)

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()

# Close driver
time.sleep(5)
driver.quit()
