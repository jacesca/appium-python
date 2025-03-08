# Follow instructions: https://appium.github.io/appium-xcuitest-driver/latest/preparation/real-device-config/
# Not working

import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


desired_caps = {}
desired_caps['platformName'] = 'IOS'
desired_caps['platformVersion'] = '18.2'
desired_caps['deviceName'] = "Jacqueline Escalante's iPhone"
desired_caps['automationName'] = 'XCUITest'
desired_caps['xcodeOrgId'] = "945DY8RP35"   # TeamID from developer.apple.com >> account >> membership   # noqa
desired_caps['xcodeSigningId'] = 'iPhone Developer'
desired_caps['updatedWDABundleId'] = 'com.testapp.jacesca'
desired_caps['udid'] = '00008120-001969A03AC2601E'   # xcrun xctrace list devices   # noqa
desired_caps['noReset'] = 'true'
desired_caps['app'] = "/Users/j.escalante/Documents/Courses/Appium-Python/Apps/UIKitCatalog.app"   # noqa
desired_caps['newCommandTimeout'] = 600

options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=options, direct_connection=True)   # noqa

ele_id = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Date Picker") # By ACCESSIBILITY_ID   # noqa
print(f"""
Text on the button (first method) : {ele_id.text}
Description of the button         : {ele_id.get_attribute('name')}
""")
ele_id.click()

time.sleep(5)
driver.quit()
