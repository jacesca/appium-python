from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.common import AppiumOptions
from configurationfiles.GlobalVariables import (APPIUM_SERVER_URL,
                                                SAUCE_USERNAME,
                                                SAUCE_ACCESSKEY,
                                                SAUCE_ONDEMAND_URL,
                                                APP_BUILD,
                                                TEST_NAME,
                                                TEST_TAGS)


class CustomDriver:
    """Create the mobile driver"""

    sauce_username = SAUCE_USERNAME
    sauce_accesskey = SAUCE_ACCESSKEY
    sauce_url = SAUCE_ONDEMAND_URL
    app_build = APP_BUILD
    test_name = TEST_NAME
    test_tags = TEST_TAGS

    def get_local_driver(self, device='GalaxyS23', desired_caps=None):
        """Configure the driver for the defined device.
        Device accept one of the following values:
        `IOS18`, `GalaxyS23`, `Pixel3XL`, `custom`
        When Custom is selected, desired_caps need to be provided"""
        # Step 2: Web Driver Object
        if device == 'GalaxyS23':
            desired_caps = self._GalaxyS23()
        elif device == 'Pixel3XL':
            desired_caps = self._Pixel3XL()
        elif device == 'custom':
            desired_caps = desired_caps
        elif device == 'IOS18':
            desired_caps = self._IOS18()
        else:
            raise "Device does not exist!"
        options = UiAutomator2Options().load_capabilities(desired_caps)
        driver = webdriver.Remote(
            APPIUM_SERVER_URL,
            options=options,
            direct_connection=True
        )
        return driver

    def _IOS18(
        self,
        app_name='/Users/j.escalante/Documents/Courses/Appium-Python/Apps/UIKitCatalog.app',   # noqa
    ):
        """Set the capabilities for the Phisical Device: Galaxy S23"""
        # Step 1: Create "Desired Capabilities"
        desired_caps = {}
        desired_caps['platformName'] = 'IOS'
        desired_caps['automationName'] = 'XCUITest'
        desired_caps['platformVersion'] = '18.1'
        desired_caps['deviceName'] = 'iPhone 16 Pro'
        desired_caps['app'] = app_name
        desired_caps['newCommandTimeout'] = 600
        return desired_caps

    def _GalaxyS23(
        self,
        app_name='/Users/j.escalante/Documents/Courses/Appium-Python/Apps/Android_Demo_App.apk',   # noqa
        app_pkg='com.code2lead.kwad',
        app_activity='com.code2lead.kwad.MainActivity'
    ):
        """Set the capabilities for the Phisical Device: Galaxy S23"""
        # Step 1: Create "Desired Capabilities"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['platformVersion'] = '14'
        desired_caps['deviceName'] = 'Galaxy S23'
        desired_caps['app'] = app_name
        desired_caps['appPackage'] = app_pkg
        desired_caps['appActivity'] = app_activity
        desired_caps['newCommandTimeout'] = 600
        return desired_caps

    def _Pixel3XL(
        self,
        app_name='/Users/j.escalante/Documents/Courses/Appium-Python/Apps/Android_Demo_App.apk',   # noqa
        app_pkg='com.code2lead.kwad',
        app_activity='com.code2lead.kwad.MainActivity'
    ):
        """Set the capabilities for the Virtual Device: Pixel 3XL"""
        # Step 1 : Create "Desired Capabilities"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['platformVersion'] = '15'
        desired_caps['deviceName'] = 'sdk_gphone64_arm64'
        desired_caps['app'] = app_name
        desired_caps['appPackage'] = app_pkg
        desired_caps['appActivity'] = app_activity
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
        caps['sauce:options']['username'] = self.sauce_username
        caps['sauce:options']['accessKey'] = self.sauce_accesskey
        caps['sauce:options']['build'] = self.app_build
        caps['sauce:options']['name'] = self.test_name
        caps['tags'] = self.test_tags
        caps['sauce:options']['deviceOrientation'] = 'PORTRAIT'

        # Converts capabilities to AppiumOptions instance
        appium_options = AppiumOptions()
        appium_options.load_capabilities(caps)
        # AppiumConnection(remote_server_addr=command_executor, client_config=client_config)   # noqa
        # start the session
        driver = webdriver.Remote(
            self.sauce_url,
            options=appium_options,
            keep_alive=True
        )
        return driver
