"""Launch USB Connected Device, Run Demo App and click on EnterValue btn.
"""
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options


# Step 1: Create "Desired Capabilities"
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '14'
desired_caps['deviceName'] = 'Galaxy S23'
desired_caps['app'] = '/Users/j.escalante/Documents/Courses/Appium-Python/Apps/Android_Demo_App.apk'   # noqa
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'
desired_caps['newCommandTimeout'] = 600

# Step 2: Web Driver Object
options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=options, direct_connection=True)   # noqa

# Step 3: "Click on the App"
ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
ele_id.click()

# Step 4 : Wait for 2 seconds
time.sleep(2)

# Step 5 : Close the driver object
driver.quit()
