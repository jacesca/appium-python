"""Perform the following actions:
- Open Wikipedia page in Safari Browser.
- Look for Albert Einstein.
In this case, we are going to change the 
context to work with webview.
"""
import time
from appium.webdriver.common.appiumby import AppiumBy
from devices.AvailableDevices import GetDriver, IOS18
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException,
                                        NoSuchElementException)


# Step 1: Create "Desired Capabilities"
# Step 2: Web Driver Object 
desired_capabilities = IOS18()
desired_capabilities['autoWebview'] = "true"
desired_capabilities['browserName'] = "safari"
del desired_capabilities['app']
driver = GetDriver(device='custom', desired_caps=desired_capabilities)

# Step 3: Explicit Wait Object
wait = WebDriverWait(
    driver=driver,
    timeout=25,
    poll_frequency=1,
    ignored_exceptions=[
        ElementNotVisibleException,
        ElementNotSelectableException,
        NoSuchElementException
    ]
)

# Step 4: Review context in app
app_contexts = driver.contexts
print(f'App Context  : {app_contexts}')  # 'NATIVE_APP', 'WEBVIEW_17505.1'

# Step 5: Launch URL
driver.get('https://www.wikipedia.org/')

# Step 6: Switch to WEBVIEW
for app_type in app_contexts:
    if "WEBVIEW" in app_type:
        driver.switch_to.context(app_type)

# Step 7: Perform the testing on the URL
cur_ele = wait.until(lambda x: x.find_element(AppiumBy.ID, 'searchInput'))
cur_ele.click()
cur_ele.send_keys('Albert Einstein')
driver.hide_keyboard(key_name='Search', strategy='topOutside')

# Step 8: Switch back to NATIVE_APP
for app_type in app_contexts:
    if "NATIVE_APP" == app_type:
        driver.switch_to.context(app_type)

# Step 7: Close the driver object
time.sleep(5)
driver.quit()
