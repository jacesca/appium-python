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

# Device size
device_size = driver.get_window_size()
print(f'''
Device width and height: {device_size}
''')

# to use with the swap
screen_width = device_size.get('width')
screen_height = device_size.get('height')
inix = screen_width * 8 / 9
endx = screen_width / 9
iniy = screen_height / 2
endy = screen_height / 2

# Swipe to Left
driver.swipe(inix, iniy, endx, endy, duration=300)
time.sleep(2)
# Swipe to Right
driver.swipe(endx, endy, inix, iniy, duration=300)
# More: https://monfared.medium.com/gestures-in-appium-part5-swipe-vertical-horizontal-df8d5870d305

# Step 4: Close the driver object
time.sleep(5)
driver.quit()
