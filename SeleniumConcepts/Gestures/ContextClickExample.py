"""
Run
python -m SeleniumConcepts.Gestures.ContextClickExample
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


# Setting the driver
driver = webdriver.Chrome()

# Open the page
driver.get('https://selenium.dev/selenium/web/mouse_interaction.html')
clickable = driver.find_element(By.ID, "clickable")
ActionChains(driver).context_click(clickable).perform()

time.sleep(0.5)
assert driver.find_element(By.ID, "click-status").text == "context-clicked"
driver.find_element(By.ID, "click-status").click()
clickable.click()
clickable.send_keys('TEST')
ActionChains(driver).double_click(clickable).perform()

# Close driver
time.sleep(5)
driver.quit()
