"""
Run
python -m SeleniumConcepts.Navigation.AlertsHandled
"""
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,
                                        NoSuchElementException)
from selenium.webdriver.support import expected_conditions as EC


# Get the driver
driver = webdriver.Chrome()
wait = WebDriverWait(
    driver=driver,
    timeout=25,
    poll_frequency=1,
    ignored_exceptions=[ElementNotVisibleException, NoSuchElementException]
)

# Open the site
driver.get("http://www.dummypoint.com/seleniumtemplate.html")
assert "Selenium Template" in driver.title


# Wait until Window menu is available to clic on it
wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Windows"))).click()


# Opening and closing a normal alerts
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[name=alertbutton]"))).click()   # noqa
time.sleep(2)
alert = wait.until(lambda d: d.switch_to.alert)
alert.accept()
time.sleep(2)

# Opening and canceling a prompt alerts
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[name=promtalertb]"))).click()   # noqa
time.sleep(2)
alert = wait.until(lambda d: d.switch_to.alert)
alert.send_keys("Canceling prompt alert")
time.sleep(2)
alert.dismiss()
time.sleep(2)

# Opening and accepting a prompt alerts
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[name=promtalertb]"))).click()   # noqa
time.sleep(2)
alert = wait.until(lambda d: d.switch_to.alert)
alert.send_keys("Accepting prompt alert")
time.sleep(2)
alert.accept()
time.sleep(2)

# Opening and canceling a confirmation alerts
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[name=confirmalertb]"))).click()   # noqa
time.sleep(2)
alert = wait.until(lambda d: d.switch_to.alert)
alert.dismiss()
time.sleep(2)

# Opening and accepting a confirmation alerts
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[name=confirmalertb]"))).click()   # noqa
time.sleep(2)
alert = wait.until(lambda d: d.switch_to.alert)
alert.accept()
time.sleep(2)


# Close driver
time.sleep(5)
driver.quit()
