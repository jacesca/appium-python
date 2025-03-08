"""Run
python -m AppiumConcepts.SauceLab.SouceLabDemo
"""
from appium import webdriver
from appium.options.common import AppiumOptions


SAUCE_USERNAME = "oauth-jacesca-e66ae"
SAUCE_ACCESSKEY = "d88ca88f-2e9c-4cd6-b676-12c9b0886f0a"
SAUCE_ONDEMAND_URL = 'https://ondemand.us-west-1.saucelabs.com:443/wd/hub'    # noqa
APP_BUILD = '2024'
TEST_NAME = 'SouceLabDemo'

caps = {}
caps['platformName'] = 'Android'
caps['browserName'] = 'Chrome'
caps['appium:deviceName'] = 'Android GoogleAPI Emulator'
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
driver = webdriver.Remote(SAUCE_ONDEMAND_URL, options=appium_options)

# run commands and assertions
driver.get("https://www.saucedemo.com")
title = driver.title
titleIsCorrect = "Swag Labs" in title
jobStatus = "passed" if titleIsCorrect else "failed"

# end the session
driver.execute_script('sauce:job-result=' + jobStatus)
driver.quit()
