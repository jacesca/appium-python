"""
Run
python -m SeleniumConcepts.Gestures.ActionChainsClass
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,
                                        NoSuchElementException)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


# Setting the driver
driver = webdriver.Chrome()
wait = WebDriverWait(
    driver=driver,
    timeout=25,
    poll_frequency=1,
    ignored_exceptions=[ElementNotVisibleException, NoSuchElementException]
)

# Getting the page
driver.get('http://dummypoint.com/seleniumtemplate.html')
time.sleep(2)
assert "Selenium Template" in driver.title

# Creating the objecct for ActionChain
action = ActionChains(driver)

# Double Click operation
element = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Form")))
action.double_click(element).perform()
time.sleep(2)

# Right Click operation on menu option `Form`
element = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Form")))
action.context_click(element).perform()

driver.switch_to.window(driver.window_handles[1])
action.send_keys(Keys.ARROW_DOWN).perform()

# Close driver
time.sleep(5)
driver.quit()
