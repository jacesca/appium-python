"""Launch USB Connected Device, Run Demo App, find ContactUsForm btn by INDEX and 
click on it.
"""
import time
from appium.webdriver.common.appiumby import AppiumBy
from devices.AvailableDevices import GetDriver


# Step 1: Create "Desired Capabilities"
# Step 2: Web Driver Object 
driver = GetDriver(device='GalaxyS23')

# Step 3: Action to execute
ele_index = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "index(4)")  # UiSelector()
ele_index.click()

# Step 4: Close the driver object
time.sleep(2)
driver.quit()
