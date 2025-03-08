"""Perform the following actions:
- Run Demo App on Android device.
- Find EnterValue btn and click on it. 
- Look for the Text Field and send some text.
- Delete the last 2 chars from the entered text.
- Go back.
"""
import time
from appium.webdriver.common.appiumby import AppiumBy
from devices.AvailableDevices import GetDriver


# Step 1: Create "Desired Capabilities"
# Step 2: Web Driver Object 
driver = GetDriver(device='GalaxyS23')

# Step 3: Action to execute
# Find EnterValue btn and click on it. 
ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
ele_id.click()
time.sleep(2)
# Look for the Text Field and send some text.
ele_classname = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")  # UiSelector()
ele_classname.send_keys("Skill2Lead")
# Delete the last 2 chars from the entered text.
ele_classname.click()
driver.press_keycode(67)   # KEYCODE_DEL More: https://stackoverflow.com/questions/7789826/adb-shell-input-events
time.sleep(2)
# Go back. It requires twice, first one closes the keypad and second one goes back to the main page
driver.press_keycode(4)    # KEYCODE_BACK
driver.press_keycode(4)

# Step 4: Close the driver object
time.sleep(5)
driver.quit()
