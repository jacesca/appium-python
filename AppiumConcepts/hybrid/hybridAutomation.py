"""
Prerequisites:
- Mobile Browser and ChromeDriver must be in same version
    - Mobile brower: open chrome >> settings >> about >> version
    - ChromeDriver: open terminal >> chromedriver --version
    If version are not equal, you can download it from:
        https://chromedriver.chromium.org/
    To install in Mac:
        $ brew uninstall chromedriver
        $ brew install chromedriver
        $ where chromedriver
        $ cd /opt/homebrew/bin/chromedriver   # or wherever is chromedriver
        $ xattr -d com.apple.quarantine chromedriver
        $ chromedriver --version
- Locators should be identified in web properly:
    - open chrome browser and type browser://inspect/#devices
      (https://inspector.appiumpro.com)
    - use browser inspector
"""
import time
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey
from devices.AvailableDevices import GalaxyS23, GetDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException,
                                        NoSuchElementException)
from selenium.webdriver.common.keys import Keys


# Step 1: Create "Desired Capabilities"
# Step 2: Web Driver Object
desired_capabilities = GalaxyS23(
    app_pkg='com.android.chrome',
    app_activity='com.google.android.apps.chrome.Main'
)
driver = GetDriver(device='custom', desired_caps=desired_capabilities)
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

# Step 3: Actions in native apps
# Continue without login
cur_ele = wait.until(lambda x: x.find_element(
    AppiumBy.ID,
    'com.android.chrome:id/signin_fre_dismiss_button'
))
cur_ele.click()
# Swipe up until got it btn
cur_ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.XPATH,
        '//android.widget.ScrollView[@resource-id="com.android.chrome:id/privacy_sandbox_dialog_scroll_view"]/android.widget.LinearLayout/android.widget.ImageView[2]'   # noqa
    )
)
driver.execute_script(
    "mobile: swipeGesture",
    {
        'elementId': cur_ele,
        'direction': 'up',
        "percent": 0.98
    }
)
# Click on got it
cur_ele = wait.until(
    lambda x: x.find_element(AppiumBy.ID, 'com.android.chrome:id/ack_button')
)
cur_ele.click()
# Open the URL in browser
cur_ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID,
        'com.android.chrome:id/search_box_text'
    )
)
cur_ele.send_keys("https://google.com")
driver.press_keycode(AndroidKey.ENTER)  # 66

# Step 4: Review context in app
app_contexts = driver.contexts
print(f'App Context: {app_contexts}')  # 'NATIVE_APP', 'WEBVIEW_chrome'

# Step 5: Switch to WEBVIEW
for app_type in app_contexts:
    if app_type == "WEBVIEW_chrome":
        driver.switch_to.context(app_type)

# Step 6: Actions on WEBVIEW
# Find Search bar and search for "Italian food"
cur_ele = wait.until(
    lambda x: x.find_element(AppiumBy.XPATH, '//*[@name="q"]')
)
cur_ele.send_keys("Italian food" + Keys.ENTER)

# Step 7: Swithc back to NATIVE_APP
for app_type in app_contexts:
    if app_type == "NATIVE_APP":
        driver.switch_to.context(app_type)

# Step 8: Do testing on native app screen in chrome
# Not allow results by ubication
cur_ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.XPATH,
        '//android.widget.Button[@text="Ahora no"]'
    )
)
cur_ele.click()
# Change URL bar to `https://skill2lead.com/`
cur_ele = wait.until(
    lambda x: x.find_element(
        AppiumBy.ID,
        'com.android.chrome:id/url_bar'
    )
)
cur_ele.click()
cur_ele.send_keys("https://skill2lead.com/")
driver.press_keycode(AndroidKey.ENTER)

# Step 9: Close the driver object
time.sleep(5)
driver.quit()
