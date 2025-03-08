"""Perform the following actions:
- Run Demo App on Android device.
- Find EnterValue btn.
- Get text.
- Get content description.
- Click on it.
- Find the text field.
- Enter some text.
- Clear the entered text.
- Reenter some text again
"""
import time
from appium.webdriver.common.appiumby import AppiumBy
from devices.AvailableDevices import GetDriver


# Step 1: Create "Desired Capabilities"
# Step 2: Web Driver Object
driver = GetDriver(device='GalaxyS23')

# Step 3: Action to execute
ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
print(f"""
Text on the button (first method) : {ele_id.text}
Text on the button (second method): {ele_id.get_attribute('text')}
Description of the button         : {ele_id.get_attribute('content-desc')}
""")
ele_id.click()
time.sleep(2)

ele_classname = driver.find_element(
    AppiumBy.CLASS_NAME,
    "android.widget.EditText"
)  # UiSelector()
ele_classname.send_keys("Skill2Lead")
time.sleep(2)
ele_classname.clear()
time.sleep(2)
ele_classname.send_keys("Skill2Lead")

# Step 4: Close the driver object
time.sleep(5)
driver.quit()
