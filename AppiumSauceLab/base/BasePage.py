import allure
import time
from allure_commons.types import AttachmentType
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException,
                                        NoSuchElementException)
from utilities import CustomLogger as cl
from configurationfiles.GlobalVariables import SCREENSHOT_FOLDER   # noqa


class BasePage:
    logger = cl.custom_logger()

    def __init__(self, driver):
        self.driver = driver
        self.logger.info('Launching App')
        self.screenshot('launch_app')

    def _wait_for_element(self, locator_value, locator_type):
        locator_type = locator_type.lower()
        wait = WebDriverWait(
            driver=self.driver,
            timeout=25,
            poll_frequency=1,
            ignored_exceptions=[
                ElementNotVisibleException,
                ElementNotSelectableException,
                NoSuchElementException
            ]
        )

        if locator_type == 'id':
            element = wait.until(lambda x: x.find_element(
                AppiumBy.ID,
                locator_value
            ))
        elif locator_type == 'class':
            element = wait.until(lambda x: x.find_element(
                AppiumBy.CLASS_NAME,
                locator_value
            ))
        elif locator_type == 'description':
            element = wait.until(lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'UiSelector().description("{locator_value}")'
            ))
        elif locator_type == 'index':
            element = wait.until(lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'UiSelector().index({int(locator_value)})'
            ))
        elif locator_type == 'text':
            element = wait.until(lambda x: x.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'text("{locator_value}")'
            ))
        elif locator_type == 'xpath':
            element = wait.until(lambda x: x.find_element(
                AppiumBy.XPATH,
                locator_value
            ))
        else:
            element = None
            self.logger.info(f'Locator Value {locator_value} not found!')

        return element

    def get_element(self, locator_value, locator_type='id'):
        element = None

        try:
            locator_type = locator_type.lower()
            element = self._wait_for_element(locator_value, locator_type)
            self.logger.info(
                f"Element found with locator type `{locator_type}` "
                f"and locator value `{locator_value}`."
            )
        except Exception as e:
            self.logger.info(
                f"Element not found. Locator value: `{locator_value}`, "
                f"Locator type: `{locator_type}`, Original error: `{e}`"
            )
            self.attach_screenshot(f"GetElement_{locator_value}")
            assert False

        return element

    def click_element(self, locator_value, locator_type='id'):
        try:
            locator_type = locator_type.lower()
            element = self.get_element(locator_value, locator_type)
            element.click()
            self.logger.info(
                f"Element clicked with locator type `{locator_type}` "
                f"and locator value `{locator_value}`."
            )
        except Exception as e:
            self.logger.info(
                f"Unable to click on Element. Locator value: `{locator_value}`"
                f", Locator type: `{locator_type}`, Original error: `{e}`"
            )
            self.attach_screenshot(f"ClickElement_{locator_value}")
            assert False

    def send_text(self, text, locator_value, locator_type='id'):
        try:
            locator_type = locator_type.lower()
            element = self.get_element(locator_value, locator_type)
            element.clear()
            element.send_keys(text)
            self.logger.info(
                f"Text `{text}` send to Element with "
                f"locator type `{locator_type}` "
                f"and locator value `{locator_value}`."
            )
        except Exception as e:
            self.logger.info(
                f"Unable to send text `{text}` on Element. "
                f"Locator value: `{locator_value}`, "
                f"Locator type: `{locator_type}`, Original error: `{e}`"
            )
            self.attach_screenshot(f"SendText_{locator_value}")
            assert False

    def is_displayed(self, locator_value, locator_type='id'):
        try:
            locator_type = locator_type.lower()
            self.get_element(locator_value, locator_type)
            self.logger.info(
                f"Element with locator type `{locator_type}` "
                f"and locator value `{locator_value}` is displayed."
            )
            return True
        except Exception:
            self.logger.info(
                f"Element with locator type `{locator_type}` "
                f"and locator value `{locator_value}` is not displayed."
            )
            return False

    def _get_filename_path(self, filename):
        file_name = filename.replace(' ', '')
        file_name = f'{file_name}_{time.strftime("%Y_%m_%d_%H_%M_%S")}.png'
        file_path = f"{SCREENSHOT_FOLDER}/{file_name}"
        return file_path

    def screenshot(self, filename):
        file_path = self._get_filename_path(filename)

        try:
            self.driver.save_screenshot(filename=file_path)
            self.logger.info(f"Screenshot saved to path: `{file_path}`")
        except Exception as e:
            self.logger.info(
                f"Screenshot unable to saved to path: `{file_path}`. "
                f"Original error: `{e}`"
            )

    def attach_screenshot(self, filename):
        file_path = self._get_filename_path(filename)
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=file_path,
            attachment_type=AttachmentType.PNG
        )

    def press_keycode(self, key_code=AndroidKey.BACK):
        self.driver.press_keycode(keycode=key_code)   # AndroidKey.BACK == 4
