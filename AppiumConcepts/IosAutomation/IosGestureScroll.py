"""Perform the following actions:
- Run Demo App on Android device.
- Scroll until Web View Button.
- Click on it.
"""
import time
from appium.webdriver.common.appiumby import AppiumBy
from devices.AvailableDevices import GetDriver, IOS18


# Step 1: Create "Desired Capabilities"
# Step 2: Web Driver Object 
# desired_capabilities = IOS18()
# desired_capabilities['orientation'] = "LANDSCAPE"
# driver = GetDriver(device='custom', desired_caps=desired_capabilities)
driver = GetDriver(device='IOS18')

# Step 3: Actions to execute
# Find elements
original_ele = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Date Picker") # By ACCESSIBILITY_ID
# destination_ele = driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[18]/XCUIElementTypeOther[1]/XCUIElementTypeOther') # By XPATH (btn area)
destination_ele = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Web View") # By ACCESSIBILITY_ID (just title)
# Scroll until destination_ele
driver.scroll(
    origin_el=original_ele,
    destination_el=destination_ele,
    duration=300
)
# Click on Web View btn.
destination_ele.click()

# Step 4: Close the driver object
time.sleep(5)
driver.quit()
