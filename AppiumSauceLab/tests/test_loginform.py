"""Run
$ pytest -v -s tests/test_loginform.py

With Allure Reports
$ pytest -v -s --alluredir reports/allurereports/  tests/test_loginform.py
$ allure serve -h localhost reports/allurereports/
"""

import unittest
import pytest
from appium.webdriver.extensions.android.nativekey import AndroidKey
from pages.LoginPage import LoginForm
from utilities import CustomLogger as cl


@pytest.mark.usefixtures("before_class", "before_method")
class LoginFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_objects(self):
        self.loginform = LoginForm(self.driver)

    # @pytest.mark.run(order=3)
    def test_login1_open_form(self):
        cl.allureLogs('App launched.')
        self.loginform.click_login_btn()
        self.loginform.verify_login_page()

    # @pytest.mark.run(order=4)
    def test_login2_wrong_fill_form(self):
        self.loginform.send_username()
        self.loginform.send_wrong_pwd()
        self.loginform.submit_login_form()
        self.loginform.verify_wrong_credentials()

    # @pytest.mark.run(order=5)
    def test_login3_fill_form(self):
        self.loginform.send_username()
        self.loginform.send_pwd()
        self.loginform.submit_login_form()

    # @pytest.mark.run(order=6)
    def test_login4_valid_credentials(self):
        self.loginform.verify_not_wrong_credentials()
        self.loginform.verify_valid_credentials()

    # @pytest.mark.run(order=7)
    def test_login5_submit_admin_value(self):
        self.loginform.send_adminvalue()
        self.loginform.submit_admin_value()

    # @pytest.mark.run(order=8)
    def test_login6_able_to_return_to_main_menu(self):
        self.loginform.press_keycode(key_code=AndroidKey.BACK)
        cl.allureLogs('Returned to credential page.')
        self.loginform.press_keycode(key_code=AndroidKey.BACK)
        cl.allureLogs('Returned to main menu page.')
