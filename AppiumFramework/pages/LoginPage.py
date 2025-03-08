from AppiumFramework.base.BasePage import BasePage
from AppiumFramework.utilities import CustomLogger as cl
from AppiumFramework.configurationfiles.GlobalVariables import (VALID_ADMIN_TXT,    # noqa
                                                                VALID_LOGIN_PWD,    # noqa
                                                                VALID_LOGIN_USER)   # noqa


class LoginForm(BasePage):
    # locators values in ContactUsForm
    _login_btn_id = 'com.code2lead.kwad:id/Login'                    # id
    _login_page_title_txt = 'Login Page'                             # text
    _login_email_idx = '3'                                           # index
    _login_pwd_txt = '4'                                             # index
    _login_submit_btn_id = 'com.code2lead.kwad:id/Btn3'              # id
    _login_pass_title_txt = 'Enter Admin'                            # text
    _login_pass_enter_admin_id = 'com.code2lead.kwad:id/Edt_admin'   # id
    _login_pass_submit_btn_txt = 'SUBMIT'                            # text
    _login_fail_wrong_credentials_txt = 'Wrong Credentials'          # text

    def __init__(self, driver):
        super().__init__(driver)

    def click_login_btn(self):
        self.click_element(self._login_btn_id)
        cl.allureLogs('Clicked on Login Button.')

    def verify_login_page(self):
        displayed_flag = self.is_displayed(
            self._login_page_title_txt,
            'text'
        )
        assert displayed_flag
        cl.allureLogs('Login Page opened.')

    def send_username(self):
        self.send_text(VALID_LOGIN_USER, self._login_email_idx, "index")
        cl.allureLogs('Entered user name.')

    def send_pwd(self):
        self.send_text(VALID_LOGIN_PWD, self._login_pwd_txt, 'index')
        cl.allureLogs("Entered password.")

    def send_wrong_pwd(self):
        self.send_text('VALID_LOGIN_PWD', self._login_pwd_txt, 'index')
        cl.allureLogs("Entered password.")

    def submit_login_form(self):
        self.screenshot('login')
        self.click_element(self._login_submit_btn_id)
        cl.allureLogs('Login Form Submit button clicked.')

    def verify_not_wrong_credentials(self):
        displayed_flag = self.is_displayed(
            self._login_fail_wrong_credentials_txt,
            'text'
        )
        assert not displayed_flag
        cl.allureLogs('Valid credentials entered.')

    def verify_valid_credentials(self):
        displayed_flag = self.is_displayed(
            self._login_pass_title_txt,
            'text'
        )
        assert displayed_flag
        cl.allureLogs('Credentials Accepted.')

    def verify_wrong_credentials(self):
        displayed_flag = self.is_displayed(
            self._login_fail_wrong_credentials_txt,
            'text'
        )
        assert displayed_flag
        cl.allureLogs('Credentials Accepted.')

    def send_adminvalue(self):
        self.send_text(VALID_ADMIN_TXT, self._login_pass_enter_admin_id)
        cl.allureLogs('Entered Admin Value.')

    def submit_admin_value(self):
        self.screenshot('AdminValue')
        self.click_element(self._login_pass_submit_btn_txt, 'text')
        cl.allureLogs('Admin Value Submitted.')
