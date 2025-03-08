"""Launch USB Connected Device, Run Demo App, find EnterValue btn by XPATH,
click on it. Then find the text field by XPATH and send some text.
"""
import time
from appium.webdriver.common.appiumby import AppiumBy
from devices.AvailableDevices import GetDriver


# Step 1: Create "Desired Capabilities"
# Step 2: Web Driver Object
driver = GetDriver(device='GalaxyS23')

# Step 3: Action to execute
# # Btn ENTER SOME VALUE - Using @content-desc
# ele_xpath = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Btn1"]')   # noqa
# # Btn ENTER SOME VALUE - Using @resource-id
# ele_xpath = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.code2lead.kwad:id/EnterValue"]')   # noqa
# # Btn ENTER SOME VALUE - Using @text
# ele_xpath = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="ENTER SOME VALUE"]')   # noqa
# Btn ENTER SOME VALUE - Using relative index value (1st item of type 'android.widget.Button')   # noqa
ele_xpath = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[1]')
# ----------------------------------------------
# # Btn SCROLLVIEW - Using relative index value (3rd item of type 'android.widget.Button')   # noqa
# ele_xpath = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[3]')
# ----------------------------------------------
ele_xpath.click()
time.sleep(2)

# TextField - Using class name, as for this case, it is equal to TagName and unique.   # noqa
ele_xpath2 = driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")  # UiSelector()   # noqa
ele_xpath2.send_keys("Skill2Lead.com")

# Step 4: Close the driver object
time.sleep(5)
driver.quit()
