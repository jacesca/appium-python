from appium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time

desired_caps = {}
desired_caps['platformName'] = 'IOS'
desired_caps['platformVersion'] = '13.3'
desired_caps['deviceName'] = 'iPhone'
desired_caps['automationName'] = 'XCUITest'
#desired_caps['xcodeOrgId'] = '10Digits_Team_ID'
desired_caps['xcodeSigningId'] = 'iPhone Developer'
#desired_caps['updatedWDABundleId'] = 'com.uicatalog.app'
desired_caps['udid'] = 'beb3dafca66b04fe33841d758847faab03846673'
desired_caps['noReset'] = 'true'
#desired_caps['app'] = ('/Users/sujithreddy/Documents/IOS_APPS/UICatalog.app')
desired_caps['autoWebview'] = 'true'
desired_caps['browserName'] = 'safari'
#desired_caps['startIWDP'] = 'true'


# 1.) Create driver object
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 2.) Explict Wait object
wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])

# 3.) Launch URL

driver.get("http://www.dummypoint.com/seleniumtemplate.html")

# 4.) Perform the testing on the URL
time.sleep(2)
ele = wait.until(lambda  x: x.find_element_by_id("user_input"))
ele.click()
ele.send_keys("Code2Lead.com")

ele2 = wait.until(lambda  x: x.find_element_by_id("submitbutton"))
ele2.click()

# 5.) Quite the driver
time.sleep(10)
driver.quit()