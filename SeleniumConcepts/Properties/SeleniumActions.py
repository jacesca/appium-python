"""
Run
python -m SeleniumConcepts.Properties.SeleniumActions
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

# Properties
print(f"""
Displayed: {element.is_displayed()}
Enabled  : {element.is_enabled()}
Size     : {element.size}
Location : {element.location}
""")

# Actions
element.click()
element.send_keys('Code2Lead')
time.sleep(2)
element.clear()
time.sleep(2)
element.send_keys('Again Code2Lead')

print(f"""
Text from `user_input` text field: {element.get_attribute('value')}
""")

time.sleep(5)
driver.quit()
