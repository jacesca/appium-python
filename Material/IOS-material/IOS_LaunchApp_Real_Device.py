from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'IOS'
desired_caps['platformVersion'] = '13.3'
desired_caps['deviceName'] = 'iPhone'
desired_caps['automationName'] = 'XCUITest'
#desired_caps['xcodeOrgId'] = '10Digits_Team_ID'
desired_caps['xcodeSigningId'] = 'iPhone Developer'
desired_caps['updatedWDABundleId'] = 'com.uicatalog.app'
desired_caps['udid'] = 'beb3dafca66b04fe33841d758847faab03846673'
desired_caps['noReset'] = 'true'
desired_caps['app'] = ('/Users/sujithreddy/Documents/IOS_APPS/UICatalog.app')


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

el = driver.find_element_by_accessibility_id('AAPLButtonViewController')  # accessibility id
el.click()
