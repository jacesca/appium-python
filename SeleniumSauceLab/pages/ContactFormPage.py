from base.BasePage import BaseClass
from selenium.webdriver.remote.webdriver import WebDriver
from utilities import CustomLogger as cl


class ContactForm(BaseClass):
    # Locators values
    _menu_form_link = 'Form'
    _form_elem_id = 'reused_form'
    _input_name_id = 'name'
    _input_email_id = 'email'
    _radio_gender_css = 'input#g[value="female"]'
    _input_tech_id = 'tech'
    _textarea_msg_id = 'message'
    _captcha_img_id = 'captcha_image'
    _input_captcha_id = 'captcha'
    _btn_postit_id = 'btnContactUs'

    def __init__(self, driver: WebDriver, url: str) -> None:
        super().__init__(driver, url)

    def click_on_form_menu_option(self) -> None:
        self.click_on_element(locator_value=self._menu_form_link,
                              locator_type='link_text')
        cl.allureLogs('Clicked on Contact Form Menu Option.')

    def verify_form_page_is_displayed(self) -> None:
        is_displayed = self.is_displayed(locator_value=self._form_elem_id)
        assert is_displayed
        cl.allureLogs('Verified Contact Form.')

    def enter_name(self) -> None:
        self.send_text(text='Code2Lead',
                       locator_value=self._input_name_id)
        cl.allureLogs('Entered name.')

    def enter_email(self) -> None:
        self.send_text(text='Code2Lead@gmail.com',
                       locator_value=self._input_email_id)
        cl.allureLogs('Entered email.')

    def select_female_gender(self) -> None:
        self.click_on_element(locator_value=self._radio_gender_css,
                              locator_type='css_selector')
        cl.allureLogs('Entered gender.')

    def enter_technology(self) -> None:
        self.send_text(text='Selenium Appium Python',
                       locator_value=self._input_tech_id)
        cl.allureLogs('Entered technology.')

    def enter_message(self) -> None:
        self.send_text(text='Message to Code2Lead',
                       locator_value=self._textarea_msg_id)
        cl.allureLogs('Entered Message.')

    def get_captcha_text(self) -> str:
        captcha_text = self.get_text(locator_value=self._captcha_img_id)
        cl.allureLogs('Got the captcha text.')
        return captcha_text

    def enter_captcha_text(self) -> None:
        self.send_text(text=self.get_captcha_text(),
                       locator_value=self._input_captcha_id)
        cl.allureLogs('Entered the captcha data.')

    def submit_contact_form(self) -> None:
        self.scroll_to(locator_value=self._btn_postit_id)
        self.click_on_element(locator_value=self._btn_postit_id)
        cl.allureLogs('Submitted contact form.')
