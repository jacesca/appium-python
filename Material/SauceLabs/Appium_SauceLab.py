from appium import  webdriver
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time

caps = {}
caps['appiumVersion'] = "1.17.1"
caps['deviceName'] = "Google Pixel 3a XL GoogleAPI Emulator"
caps['deviceOrientation'] = "portrait"
caps['platformVersion'] = "10.0"
caps['platformName'] = "Android"
caps['app'] = "storage:filename=Android_Demo_App.apk"


url = "https://sujiXXXX:ad94c954-xxxx-4994-8339-xxxxxxxx@ondemand.us-west-1.saucelabs.com:443/wd/hub"

driver =webdriver.Remote(url,caps,keep_alive=True)

#list of Selenium Exceptions
#https://www.selenium.dev/selenium/docs/api/py/common/selenium.common.exceptions.html
wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])



ele = wait.until(lambda  x: x.find_element_by_id("com.code2lead.kwad:id/EnterValue"))
ele.click()

time.sleep(4)
driver.quit()