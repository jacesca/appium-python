"""
Run
python -m SeleniumConcepts.Locators.FindElementBy
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('http://dummypoint.com/seleniumtemplate.html')
time.sleep(2)

# Locators
driver.find_element(By.ID, "user_input").send_keys('Code2Lead')
time.sleep(2)
driver.find_element(By.CLASS_NAME, "entertext").send_keys('_ClassName')   # noqa
time.sleep(2)
driver.find_element(By.NAME, "textbox").send_keys('_NAME')   # noqa
time.sleep(2)
driver.find_elements(By.TAG_NAME, "input")[1].send_keys('_TagName')   # noqa
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Form").click()   # noqa
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "Locat").click()   # noqa

time.sleep(5)
driver.quit()
