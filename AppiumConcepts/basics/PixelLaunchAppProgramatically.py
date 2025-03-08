"""Start Appium Service, Launch USB Connected Device, Run Demo App and click
on  EnterValue btn.
Run
cd AppiumConcepts
python -m basics.PixelLaunchAppProgramatically
"""
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService


# Step 1: Create object for Appium Service Class
appium_service = AppiumService()

# Step 2: Start Appium Service
appium_service.start()

# Step 3: Create "Desired Capabilities"
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '15'
desired_caps['deviceName'] = 'sdk_gphone64_arm64'
desired_caps['app'] = '/Users/j.escalante/Documents/Courses/Appium-Python/Apps/Android_Demo_App.apk'  # noqa
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'
desired_caps['newCommandTimeout'] = 600

# Step 4: Web Driver Object
options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=options, direct_connection=True)    # noqa

# Step 5: "Click on the App"
ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
ele_id.click()

# Step 6: Wait for 2 seconds
time.sleep(2)

# Step 7: Close the driver object
driver.quit()

# Step 8: Stop Appium Service
appium_service.stop()
