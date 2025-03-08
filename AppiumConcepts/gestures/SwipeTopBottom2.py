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
                                                       'new UiScrollable(new UiSelector()).scrollIntoView(text("ScrollView"))'))
ele_btn.click()

# Swipe to Up
btn = wait.until(lambda  x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'text("BUTTON1")'))
time.sleep(2)
driver.execute_script("mobile: swipeGesture", {'elementId':btn, 'direction':'up', "percent":0.98})
time.sleep(2)

# Swipe to Down
btn = wait.until(lambda  x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'text("BUTTON12")'))
print(btn.is_displayed())
time.sleep(2) 
driver.execute_script("mobile: swipeGesture", {'elementId':btn, 'direction':'down', "percent":0.98})

# Step 4: Close the driver object
time.sleep(5)
driver.quit()
