"""Start Appium Service, Launch USB Connected Device, Run Demo App, click on 
EnterValue btn.
Once automation end, close app and Stop Appium Service.
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

try:
    # Step 3: Create "Desired Capabilities"
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['automationName'] = 'UiAutomator2'
    desired_caps['platformVersion'] = '15'
    desired_caps['deviceName'] = 'sdk_gphone64_arm64'
    desired_caps['app'] = '/Users/j.escalante/Documents/Courses/Appium-Python/Apps/Android_Demo_App.apk'
    desired_caps['appPackage'] = 'com.android.chrome'
    desired_caps['appActivity'] = 'com.google.android.apps.chrome.Main'
    desired_caps['newCommandTimeout'] = 600
    
    # Step 4: Web Driver Object 
    options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:4723', options=options, direct_connection=True)
    
    # Step 5: Wait for 5 seconds
    time.sleep(5)
    
    # Step 6: Close the driver object
    driver.quit()

except Exception as e:
    print(e)

finally:
    # Step 7: Stop Appium Service
    appium_service.stop()
