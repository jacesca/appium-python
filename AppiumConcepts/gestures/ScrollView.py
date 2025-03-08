"""Perform the following actions, using explicit wait.
- Run Demo App on Android device.
- Find ScrollView btn and click on it. 
- Scroll until Button12.
- Click on it.
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
ele_id = wait.until(lambda device: device.find_element(AppiumBy.ID, "com.code2lead.kwad:id/ScrollView"))
ele_id.click()
ele_id = wait.until(lambda device: device.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                       'new UiScrollable(new UiSelector()).scrollIntoView(text("BUTTON12"))'))
ele_id.click()

# Step 4: Close the driver object
time.sleep(2)
driver.quit()
