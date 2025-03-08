"""Run
python -m AppiumConcepts.SauceLab.AppiumSauceLab

Prerrequisites:
- App need to be uploaded to SauceLab
"""
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException,
                                        NoSuchElementException)
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.common import AppiumOptions


SAUCE_USERNAME = "oauth-jacesca-e66ae"
SAUCE_ACCESSKEY = "d88ca88f-2e9c-4cd6-b676-12c9b0886f0a"
SAUCE_ONDEMAND_URL = 'https://ondemand.us-west-1.saucelabs.com:443/wd/hub'    # noqa
APP_BUILD = '2024'
TEST_NAME = 'AppiumConcept'


class DeviceConfiguration:
    def __init__(
        self,
        app_name='/Users/j.escalante/Documents/Courses/Appium-Python/Apps/Android_Demo_App.apk',   # noqa
        app_pkg='com.code2lead.kwad',
        app_activity='com.code2lead.kwad.MainActivity'
    ):
        self.app_name = app_name
        self.app_pkg = app_pkg
        self.app_activity = app_activity

    def ios_18(
        self,
        app_name='/Users/j.escalante/Documents/Courses/Appium-Python/Apps/UIKitCatalog.app',   # noqa
    ):
        """Set the capabilities for the Phisical Device: Galaxy S23"""
        self.app_name = app_name

        # Step 1: Create "Desired Capabilities"
        desired_caps = {}
        desired_caps['platformName'] = 'IOS'
        desired_caps['automationName'] = 'XCUITest'
        desired_caps['platformVersion'] = '18.1'
        desired_caps['deviceName'] = 'iPhone 16 Pro'
        desired_caps['app'] = self.app_name
        desired_caps['newCommandTimeout'] = 600
        return desired_caps

    def galaxy_s23(self):
        """Set the capabilities for the Phisical Device: Galaxy S23"""
        # Step 1: Create "Desired Capabilities"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['platformVersion'] = '14'
        desired_caps['deviceName'] = 'Galaxy S23'
        desired_caps['app'] = self.app_name
        desired_caps['appPackage'] = self.app_pkg
        desired_caps['appActivity'] = self.app_activity
        desired_caps['newCommandTimeout'] = 600
        return desired_caps

    def pixel_3xl(self):
        """Set the capabilities for the Virtual Device: Pixel 3XL"""
        # Step 1 : Create "Desired Capabilities"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['platformVersion'] = '15'
        desired_caps['deviceName'] = 'sdk_gphone64_arm64'
        desired_caps['app'] = self.app_name
        desired_caps['appPackage'] = self.app_pkg
        desired_caps['appActivity'] = self.app_activity
        desired_caps['newCommandTimeout'] = 600
        return desired_caps

    def get_cloud_driver(self):
        caps = {}
        caps['platformName'] = 'Android'
        # caps['browserName'] = 'Chrome'
        caps['appium:app'] = 'storage:filename=Android_Demo_App.apk'
        caps['appium:deviceName'] = 'Google Pixel 4 XL GoogleAPI Emulator'
        caps['appium:platformVersion'] = '15.0'
        caps['appium:automationName'] = 'UiAutomator2'
        caps['sauce:options'] = {}
        caps['sauce:options']['appiumVersion'] = '2.11.0'
        caps['sauce:options']['username'] = SAUCE_USERNAME
        caps['sauce:options']['accessKey'] = SAUCE_ACCESSKEY
        caps['sauce:options']['build'] = APP_BUILD
        caps['sauce:options']['name'] = TEST_NAME
        caps['sauce:options']['deviceOrientation'] = 'PORTRAIT'

        # Converts capabilities to AppiumOptions instance
        appium_options = AppiumOptions()
        appium_options.load_capabilities(caps)

        # start the session
        driver = webdriver.Remote(
            SAUCE_ONDEMAND_URL,
            options=appium_options,
            keep_alive=True
        )
        return driver

    def get_local_driver(self, device='GalaxyS23', desired_caps=None):
        # Step 2: Web Driver Object
        if device == 'GalaxyS23':
            desired_caps = self.galaxy_s23()
        elif device == 'Pixel3XL':
            desired_caps = self.pixel_3xl()
        elif device == 'custom':
            desired_caps = desired_caps
        elif device == 'IOS18':
            desired_caps = self.ios_18()
        else:
            raise "Device does not exist!"
        options = UiAutomator2Options().load_capabilities(desired_caps)
        driver = webdriver.Remote(
            'http://127.0.0.1:4723',
            options=options,
            direct_connection=True
        )
        return driver


# Step 1: Create "Desired Capabilities"
# Step 2: Web Driver Object
# driver = DeviceConfiguration().get_local_driver(device='Pixel3XL')    # local
driver = DeviceConfiguration().get_cloud_driver()    # cloud
wait = WebDriverWait(
    driver=driver,
    timeout=25,
    poll_frequency=1,
    ignored_exceptions=[
        ElementNotVisibleException,
        ElementNotSelectableException,
        NoSuchElementException
    ]
)

# Step 3: Action to execute
ele_id = wait.until(lambda device: device.find_element(
    AppiumBy.ID,
    "com.code2lead.kwad:id/EnterValue"
))
ele_id.click()

time.sleep(2)
ele_classname = wait.until(lambda device: device.find_element(
    AppiumBy.CLASS_NAME,
    "android.widget.EditText"
))
ele_classname.send_keys("Skill2Lead")

# Step 4: Close the driver object
time.sleep(5)
jobStatus = 'passed'    # or 'failed'
driver.execute_script('sauce:job-result=' + jobStatus)
driver.quit()
