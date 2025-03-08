from base.BasePage import BaseClass
from selenium.webdriver.remote.webdriver import WebDriver
from utilities import CustomLogger as cl


class EnterTextPage(BaseClass):
    # Locators values
    _menu_loctors_link = 'Locators'
    _input_text_id = 'user_input'
    _btn_submit_id = 'submitbutton'

    def __init__(self, driver: WebDriver, url: str) -> None:
        super().__init__(driver, url)

    def click_on_locator_menu_option(self) -> None:
        self.click_on_element(locator_value=self._menu_loctors_link,
                              locator_type='link_text')
        cl.allureLogs('Clicked on Locator Menu Option.')

    def enter_text(self) -> None:
        self.send_text(text='Code2Lead',
                       locator_value=self._input_text_id)
        cl.allureLogs('Entered text.')

    def submit_enter_text_form(self) -> None:
        self.scroll_to(locator_value=self._btn_submit_id)
        self.click_on_element(locator_value=self._btn_submit_id)
        cl.allureLogs('Submitted entered text.')
