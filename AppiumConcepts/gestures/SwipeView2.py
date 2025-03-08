"""Perform the following actions, using explicit wait.
- Run Demo App on Android device.
- Find TabActivity btn and click on it. 
- Swap from left to right.
- Swap from right to left.
"""
import time
from appium.webdriver.common.appiumby import AppiumBy
from devices.AvailableDevices import GetDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException,
                                        NoSuchElementException)


# Step 1: Create "Desired Capabilities"
# Step 2: Web Driver Object 
driver = GetDriver(device='GalaxyS23')
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

# Step 3: Action to execute
ele_btn = wait.until(lambda device: device.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                       'new UiScrollable(new UiSelector()).scrollIntoView(text("TAB ACTIVITY"))'))
ele_btn.click()

# Swipe to Left
hometab = wait.until(lambda  x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'text("HomeFragment")'))
time.sleep(5)
driver.execute_script("mobile: swipeGesture", {'elementId':hometab, 'direction':'left', "percent":0.98})
time.sleep(5)

# Swipe to Right
sporttab = wait.until(lambda  x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'text("SportFragment")'))
time.sleep(5) 
driver.execute_script("mobile: swipeGesture", {'elementId':sporttab, 'direction':'right', "percent":0.98})

# Step 4: Close the driver object
time.sleep(5)
driver.quit()
