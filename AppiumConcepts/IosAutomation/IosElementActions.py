"""Perform the following actions:
- Run Demo App on Android device.
- Get back some element properties of Date Picker btn.
"""
import time
from appium.webdriver.common.appiumby import AppiumBy
from devices.AvailableDevices import GetDriver, IOS18


# Step 1: Create "Desired Capabilities"
# Step 2: Web Driver Object 
driver = GetDriver(device='IOS18')

# Step 3: Actions to execute
ele_id = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Date Picker") # By ACCESSIBILITY_ID
print(f"""
Text on the button (first method) : {ele_id.text}
Description of the button         : {ele_id.get_attribute('name')} 
""")

# Step 4: Close the driver object
time.sleep(5)
driver.quit()
