"""Launch USB Connected Device, Run Demo App, find all btn items.
Then click on the ScrollView btn.
"""
import time
from appium.webdriver.common.appiumby import AppiumBy
from devices.AvailableDevices import GetDriver


# Step 1: Create "Desired Capabilities"
# Step 2: Web Driver Object 
driver = GetDriver(device='GalaxyS23')

# Step 3: Action to execute
elements = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Button")
for btn in elements:
    print(btn.text)

for btn in elements:
    if btn.text == "ScrollView":
        btn.click()
        break

# Step 4: Close the driver object
time.sleep(5)
driver.quit()
