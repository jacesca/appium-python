from selenium import webdriver
import time

from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec

sauce_username = "code2lead"
sauce_access_key = "xxxxxxxx-xxxx-4994-8339-xxxxxxxxxxxx"

SauceOptions={
    'name':'Dummy Point Test in Mac',
    'build': 'Dummypoint Regression Test',
    'screenResolution':'1024x768',
    'username': sauce_username,
    'accessKey': sauce_access_key,
    # tags to filter test reporting.
    'tags': ['instant-sauce', 'pytest', 'module4'],
}

capabilities = {
  'browserName': 'chrome',
  'browserVersion': 'latest',
  'platformName': 'macOS 10.15',
  'sauce:options': SauceOptions
}


url = "https://ondemand.saucelabs.com:443/wd/hub"


driver = webdriver.Remote(command_executor=url,desired_capabilities=capabilities,keep_alive=True)

driver.get("http://www.dummypoint.com/seleniumtemplate.html")
time.sleep(2)

wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])
ele = wait.until(ec.presence_of_element_located((By.ID,"user_input")))
ele.send_keys("Code2Lead")

time.sleep(5)
driver.quit()