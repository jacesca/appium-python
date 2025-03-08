"""
Run
python -m SeleniumConcepts.Gestures.ScrollByWaitExplicit
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,
                                        NoSuchElementException)
from selenium.webdriver.support import expected_conditions as EC


# Step 1: Getting the driver
driver = webdriver.Chrome()
driver.get('http://dummypoint.com/seleniumtemplate.html')
time.sleep(2)
wait = WebDriverWait(
    driver=driver,
    timeout=25,
    poll_frequency=1,
    ignored_exceptions=[ElementNotVisibleException, NoSuchElementException]
)

# Step 2: Confirming the page
assert "Selenium Template" in driver.title

# Step 3: Actions
# Click on Form
wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Form"))).click()
# Wait until form is loaded
wait.until(EC.presence_of_element_located((By.ID, "reused_form")))
# Fill the form
wait.until(EC.presence_of_element_located((By.ID, "name"))).send_keys('Lead2CodeName')   # noqa
time.sleep(2)
wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys('Lead2Code@email.com')   # noqa
time.sleep(2)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#g[value="female"]'))).click()   # noqa
time.sleep(2)
wait.until(EC.presence_of_element_located((By.ID, "tech"))).send_keys('Selenium')   # noqa
time.sleep(2)
wait.until(EC.presence_of_element_located((By.ID, "message"))).send_keys('Message Text')   # noqa
time.sleep(2)
catchap_text = wait.until(EC.presence_of_element_located((By.ID, "captcha_image"))).text   # noqa
time.sleep(2)
wait.until(EC.presence_of_element_located((By.ID, "captcha"))).send_keys(catchap_text)   # noqa
# Submit the form
time.sleep(5)
wait.until(EC.presence_of_element_located((By.ID, "btnContactUs"))).click()   # noqa

# Step 4: Close driver
time.sleep(5)
driver.quit()
