from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver = webdriver.Chrome("/Users/sujithreddy/Documents/Code2Lead/drivers/chromedriver")

driver.get("http://www.dummypoint.com/Actions.html")
assert "Selenium Template" in driver.title
time.sleep(2)

wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])

ele = wait.until(ec.presence_of_element_located((By.LINK_TEXT,"FORM")))

# Import the ActionChains Class

# 1. Create the object for ActionChains class
actions = ActionChains(driver)


# 2. Double click Operation
actions.double_click(ele).perform()



# 3. Right click Operation
#actions.context_click().perform()
#actions.context_click(ele).perform()


time.sleep(5)
driver.quit()
