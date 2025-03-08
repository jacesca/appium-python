
from appium import webdriver
from appium.options.android import UiAutomator2Options


def IOS18(
    app_name='/Users/j.escalante/Documents/Courses/Appium-Python/Apps/UIKitCatalog.app',
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


def GalaxyS23(
    app_name='/Users/j.escalante/Documents/Courses/Appium-Python/Apps/Android_Demo_App.apk',
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


def Pixel3XL(
    app_name='/Users/j.escalante/Documents/Courses/Appium-Python/Apps/Android_Demo_App.apk',
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


def GetDriver(device='GalaxyS23', desired_caps=None):
    """Configure the driver for the defined device.
    Device accept one of the following values: `IOS18`, `GalaxyS23`, `Pixel3XL`, `custom`
    When Custom is selected, desired_caps need to be provided"""
    # Step 2: Web Driver Object 
    if device == 'GalaxyS23':
        desired_caps = GalaxyS23()
    elif device == 'Pixel3XL':
        desired_caps = Pixel3XL()
    elif device == 'custom':
        desired_caps = desired_caps
    elif device == 'IOS18':
        desired_caps = IOS18()
    else:
        raise "Device does not exist!"
    options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:4723', options=options, direct_connection=True)
    return driver
