import time
import allure
from allure_commons.types import AttachmentType
from traceback import extract_stack, print_stack
from configurationfiles.GlobalVariables import SCREENSHOT_FOLDER    # noqa
from utilities import CustomLogger as cl
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from typing import Literal
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,
                                        NoSuchElementException)
from selenium.webdriver.support import expected_conditions as EC


class BaseClass:
    logger = cl.custom_logger()
    locator_type_dict = {
        'id': By.ID,
        'name': By.NAME,
        'class_name': By.CLASS_NAME,
        'xpath': By.XPATH,
        'css_selector': By.CSS_SELECTOR,
        'tag_name': By.TAG_NAME,
        'link_text': By.LINK_TEXT,
        'partial_link_text': By.PARTIAL_LINK_TEXT
    }
    LocatorType = Literal[
            'id',
            'name',
            'class_name',
            'xpath',
            'css_selector',
            'tag_name',
            'link_text',
            'partial_link_text'
        ]

    def __init__(self, driver: WebDriver, url: str) -> None:
        self.driver = driver
        self.wait = WebDriverWait(
            driver=self.driver,
            timeout=25,
            poll_frequency=1,
            ignored_exceptions=[ElementNotVisibleException,
                                NoSuchElementException]
        )
        self.url = url

    def _get_locator_type(self, locator_type: LocatorType) -> By:
        locator_type = locator_type.lower()
        if locator_type in self.locator_type_dict:
            return self.locator_type_dict[locator_type]
        else:
            self.logger.error(f'Locator type `{locator_type}` does not found.')
            return None

    def _log_exception(self, custom_msg: str, error_msg: str) -> None:
        trace = extract_stack()
        self.logger.error(
            f'{custom_msg}. Original Error: {error_msg}. Trace: {trace}'
        )
        print_stack()

    def launch_webpage(self, title: str) -> None:
        try:
            self.driver.get(self.url)

            assert title in self.driver.title

            self.logger.info(f"Web page launched with url: `{self.url}`.")
        except AssertionError as e:
            self._log_exception(
                custom_msg=f'Title page does not contains: `{title}`',
                error_msg=str(e)
            )
            self.attach_screenshot("title page")
            assert False
        except Exception as e:
            self._log_exception(
                custom_msg=f'Unable to launch web page with url: `{self.url}`',
                error_msg=str(e)
            )
            self.attach_screenshot("Launch webpage")
            assert False

    def get_webelement(self, locator_value: str, locator_type: LocatorType = 'id') -> WebElement:   # noqa
        try:
            locator_by = self._get_locator_type(locator_type)
            web_element = self.driver.find_element(locator_by, locator_value)
            self.logger.info(
                f'Web element found with locator type: `{locator_type}` '
                f'and locator value: `{locator_value}`.'
            )
            return web_element
        except Exception as e:
            self._log_exception(
                custom_msg='Web element not found with locator type: '
                           f'`{locator_type}` and locator value: '
                           f'`{locator_value}`',
                error_msg=str(e)
            )
            self.attach_screenshot(f"get_webelement_{locator_type}")
            assert False

    def wait_for_element(self, locator_value: str, locator_type: LocatorType = 'id') -> WebElement:   # noqa
        try:
            locator_by = self._get_locator_type(locator_type)
            web_element = self.wait.until(
                EC.presence_of_element_located((locator_by, locator_value))
            )
            self.logger.info(
                'Web element (wait approach) found with locator type: '
                f'`{locator_type}` and locator value: `{locator_value}`.'
            )
            return web_element
        except Exception as e:
            self._log_exception(
                custom_msg='Web element (wait approach) not found with locator'
                           f' type: `{locator_type}` and locator value: '
                           f'`{locator_value}`',
                error_msg=str(e)
            )
            self.attach_screenshot(f"wait_for_element_{locator_type}")
            assert False

    def click_on_element(self, locator_value: str, locator_type: LocatorType = 'id') -> None:   # noqa
        try:
            web_element = self.wait_for_element(locator_value, locator_type)
            web_element.click()
            self.logger.info(
                f'Clicked on web element with locator type: `{locator_type}` '
                f'and locator value: `{locator_value}`.'
            )
        except Exception as e:
            self._log_exception(
                custom_msg='Unable to click on web element with locator type: '
                           f'`{locator_type}` and locator value: '
                           f'`{locator_value}`',
                error_msg=str(e)
            )
            self.attach_screenshot(f"click_element_{locator_type}")
            assert False

    def send_text(self, text: str, locator_value: str, locator_type: LocatorType = 'id') -> None:   # noqa
        try:
            web_element = self.wait_for_element(locator_value, locator_type)
            web_element.send_keys(text)
            self.logger.info(
                f'Text `{text}` send on web element with locator type: '
                f'`{locator_type}` and locator value: `{locator_value}`.'
            )
        except Exception as e:
            self._log_exception(
                custom_msg=f'Unable to send text `{text}` on web element with '
                           f'locator type: `{locator_type}` and locator value:'
                           f' `{locator_value}`',
                error_msg=str(e)
            )
            self.attach_screenshot(f"send_text_{locator_type}")
            assert False

    def get_text(self, locator_value: str, locator_type: LocatorType = 'id') -> str:   # noqa
        element_txt = None
        try:
            web_element = self.wait_for_element(locator_value, locator_type)
            element_txt = web_element.text
            self.logger.info(
                f'Got the text `{element_txt}` from web element with locator '
                f'type: `{locator_type}` and locator value: `{locator_value}`.'
            )
        except Exception as e:
            self._log_exception(
                custom_msg='Unable to got the text from web element with '
                           f'locator type: `{locator_type}` and locator value:'
                           f' `{locator_value}`',
                error_msg=str(e)
            )
            self.attach_screenshot(f"get_text_{locator_type}")
            assert False
        return element_txt

    def is_displayed(self, locator_value: str, locator_type: LocatorType = 'id') -> bool:   # noqa
        displayed = False
        try:
            web_element = self.wait_for_element(locator_value, locator_type)
            displayed = web_element.is_displayed()
            self.logger.info(
                f'Displayed {displayed} web element with locator '
                f'type: `{locator_type}` and locator value: `{locator_value}`.'
            )
        except Exception as e:
            self._log_exception(
                custom_msg='Unable to evaluate is_displayed on web element '
                           f'with locator type: `{locator_type}` and locator '
                           f'value: `{locator_value}`',
                error_msg=str(e)
            )
            self.attach_screenshot(f"is_displayed_{locator_type}")
            assert False
        return displayed

    def scroll_to(self, locator_value: str, locator_type: LocatorType = 'id') -> None:   # noqa
        try:
            destination = self.wait_for_element(locator_value, locator_type)
            ActionChains(self.driver).move_to_element(destination).perform()
            self.logger.info(
                f'Scrolled to web element with locator type: `{locator_type}` '
                f'and locator value: `{locator_value}`.'
            )
        except Exception as e:
            self._log_exception(
                custom_msg='Unable to scroll ton web element with locator '
                           f'type: `{locator_type}` and locator '
                           f'value: `{locator_value}`',
                error_msg=str(e)
            )
            self.attach_screenshot(f"scroll_to_{locator_type}")
            assert False

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
