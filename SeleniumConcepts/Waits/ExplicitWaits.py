"""
Run
python -m SeleniumConcepts.Waits.ExplicitWaits

Documentation:
- Selenium Common Exceptions: https://www.selenium.dev/selenium/docs/api/py/common/selenium.common.exceptions.html   # noqa
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,
                                        NoSuchElementException)
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get('http://dummypoint.com/seleniumtemplate.html')
time.sleep(2)

wait = WebDriverWait(
    driver=driver,
    timeout=25,
    poll_frequency=1,
    ignored_exceptions=[ElementNotVisibleException, NoSuchElementException]
)
element = wait.until(EC.presence_of_element_located((By.ID, "user_input")))
element.send_keys('Code2Lead')

time.sleep(5)
driver.quit()
