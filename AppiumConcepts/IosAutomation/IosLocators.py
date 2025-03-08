"""Perform the following actions:
- Run Demo App on Android device.
- And click on Date Picker Button.
"""
import time
from appium.webdriver.common.appiumby import AppiumBy
from devices.AvailableDevices import GetDriver


# Step 1: Create "Desired Capabilities"
# Step 2: Web Driver Object 
driver = GetDriver(device='IOS18')

# Step 3: Actions to execute
# ele_id = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Date Picker") # By ACCESSIBILITY_ID
# ele_id = driver.find_element(AppiumBy.ID, "Date Picker") # By ID
# ele_id = driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Date Picker"]') # By XPATH using name
# ele_id = driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@value="Date Picker"]') # By XPATH using value
ele_id = driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@label="Date Picker"]') # By XPATH using label
ele_id.click()

# Step 4: Close the driver object
time.sleep(5)
driver.quit()
