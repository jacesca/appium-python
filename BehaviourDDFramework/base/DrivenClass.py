from selenium import webdriver
from selenium.webdriver.safari.service import Service as SafariService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from configurationfiles.GlobalVariables import (CHROME_WEBDRIVER,    # noqa
                                                FIREFOX_WEBDRIVER,    # noqa
                                                SAFARI_WEBDRIVER,    # noqa
                                                SAUCE_USERNAME,    # noqa
                                                SAUCE_ACCESSKEY)    # noqa
from utilities import CustomLogger as cl
from selenium.webdriver.remote.webdriver import WebDriver


class WebDriverClient:
    driver_types = {
        "chrome": (webdriver.Chrome, webdriver.ChromeOptions, ChromeService, CHROME_WEBDRIVER),    # noqa
        "firefox": (webdriver.Firefox, webdriver.FirefoxOptions, FirefoxService, FIREFOX_WEBDRIVER),    # noqa
        "safari": (webdriver.Safari, webdriver.SafariOptions, SafariService, SAFARI_WEBDRIVER)    # noqa
    }
    logger = cl.custom_logger()

    sauce_username = SAUCE_USERNAME
    sauce_accesskey = SAUCE_ACCESSKEY

    def __init__(
        self,
        browsername: str = 'chrome',
        explicit_webdriver: bool = False
    ) -> None:
        self.browsername = browsername
        self.explicit_webdriver = explicit_webdriver

        self.logger.info(
            f'Initializing the webdriver with browser=`{self.browsername}` '
            f'and explicit_webdriver=`{self.explicit_webdriver}`.'
        )

    def _get_explicit_webdriver(self) -> WebDriver:
        executable_path = self.driver_types[self.browsername][3]
        webdriver_service = self.driver_types[self.browsername][2]
        webdriver_options = self.driver_types[self.browsername][1]
        webdriver_object = self.driver_types[self.browsername][0]

        service = webdriver_service(executable_path=executable_path)
        options = webdriver_options()
        driver = webdriver_object(options=options, service=service)
        return driver

    def _get_webdriver(self) -> WebDriver:
        webdriver_object = self.driver_types[self.browsername][0]
        driver = webdriver_object()
        return driver

    def get_webdriver(self) -> WebDriver:
        """Return webdriver.
        Input parameters:
        browsername: It can be `chrome`, `firefox`, `safari`
        explicit_webdriver: If true patht to driver will be specifid"""
        if self.explicit_webdriver:
            driver = self._get_explicit_webdriver()
        else:
            driver = self._get_webdriver()

        self.logger.info(f'WebDriver `{self.browsername}` configured!')
        return driver

    def get_cloud_driver(
        self,
        platform_name: str,
        browser_name: str,
        browser_version: str
    ) -> WebDriver:
        sauce_options = {
            'name': 'Dummy Point Test FrameWork',
            'build': 'Version 1',
            'screenResolution': '1280x768',
            'username': self.sauce_username,
            'accessKey': self.sauce_accesskey,
            # tags to filter test reporting.
            'tags': ['framework', 'pytest', 'module4'],
        }

        capabilities = {
            'browserName': browser_name,
            'browserVersion': browser_version,
            'platformName': platform_name,
            'sauce:options': sauce_options
        }

        url = "https://ondemand.saucelabs.com:443/wd/hub"

        driver = webdriver.Remote(
            command_executor=url,
            desired_capabilities=capabilities,
            keep_alive=True
        )

        return driver
