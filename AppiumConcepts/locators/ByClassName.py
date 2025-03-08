"""Launch USB Connected Device, Run Demo App, find EnterValue btn by ID, 
click on it. Then look for Text Field by CLASSNAME and send some text.
"""
import time
from appium.webdriver.common.appiumby import AppiumBy
from devices.AvailableDevices import GetDriver


# Step 1: Create "Desired Capabilities"
# Step 2: Web Driver Object 
driver = GetDriver(device='GalaxyS23')

# Step 3: Action to execute
ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
ele_id.click()
time.sleep(2)

ele_classname = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")  # UiSelector()
ele_classname.send_keys("Skill2Lead")

# Step 4: Close the driver object
time.sleep(5)
driver.quit()
