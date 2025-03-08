"""Launch USB Connected Device, Run Demo App, find ScrollView btn
by CONTENT-DESCRIPTION and click on it.
"""
import time
from appium.webdriver.common.appiumby import AppiumBy
from devices.AvailableDevices import GetDriver


# Step 1: Create "Desired Capabilities"
# Step 2: Web Driver Object
driver = GetDriver(device='GalaxyS23')

# Step 3: Action to execute
ele_description = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                      'UiSelector().description("Btn3")')   # or just 'description("Btn3")'  # noqa
ele_description.click()

# Step 4: Close the driver object
time.sleep(2)
driver.quit()
