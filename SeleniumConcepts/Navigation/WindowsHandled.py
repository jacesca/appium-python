"""
Run
python -m SeleniumConcepts.Navigation.WindowsHandled
"""
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


driver = webdriver.Chrome()

# Open the site
driver.get("http://www.dummypoint.com/Windows.html")
assert "Selenium Template" in driver.title


# To get the current window name
window_name = driver.current_window_handle
print("Window before switching:", window_name)
time.sleep(2)


# Get back all input btn
elements = driver.find_elements(By.CSS_SELECTOR, "input[value*='Open a Popup']")   # noqa
print('Available btn options:')
for element in elements:
    print('\t', element.get_attribute('value'))
time.sleep(2)


# Click on the btn `Open a Popup Window2`
driver.find_element(By.CSS_SELECTOR, "input[value='Open a Popup Window2']").click()   # noqa


# Review opened windows
windows = driver.window_handles
print('Total opened windows:', len(windows))
for window in windows:
    print('\tWindow:', window)


# Switch to the last opened window
driver.switch_to.window(windows[-1])
time.sleep(2)

window_name = driver.current_window_handle
print("After switching:", window_name)
driver.maximize_window()
time.sleep(2)

# Performing action on new windows
driver.find_element(By.CSS_SELECTOR, "input[type='search'").send_keys('Code2Lead')   # noqa
time.sleep(5)

# Close current windows and return
driver.close()
driver.switch_to.window(windows[0])
window_name = driver.current_window_handle
print("Active windows:", window_name)

# Close driver
time.sleep(5)
driver.quit()
