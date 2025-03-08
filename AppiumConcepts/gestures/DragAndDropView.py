"""Perform the following actions, using explicit wait.
- Run Demo App on Android device.
- Scroll until finding DRAGANDDROP btn, and click it.
- Drag the logo until 2nd layer. 
"""
import time
from appium.webdriver.common.appiumby import AppiumBy
from devices.AvailableDevices import GetDriver
from selenium.webdriver import ActionChains
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
ele_id = wait.until(lambda device: device.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                       'new UiScrollable(new UiSelector()).scrollIntoView(text("DRAGANDDROP"))'))
ele_id.click()
# Find elements for Drag and Drop
ele_to_move = wait.until(lambda device: device.find_element(AppiumBy.ID, "com.code2lead.kwad:id/ingvw"))
ele_destination = wait.until(lambda device: device.find_element(AppiumBy.ID, "com.code2lead.kwad:id/layout2"))
# Drag and Drop actions
action = ActionChains(driver=driver)
action.w3c_actions.pointer_action.click_and_hold(ele_to_move)
action.w3c_actions.pointer_action.pause(3)
action.w3c_actions.pointer_action.move_to(ele_destination)
action.w3c_actions.pointer_action.release()
action.perform()

# Step 4: Close the driver object
time.sleep(5)
driver.quit()
