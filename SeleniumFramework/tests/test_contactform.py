"""Run
pytest -v -s SeleniumFramework/tests/test_contactform.py

With Allure Reports
pytest -v -s --alluredir SeleniumFramework/reports/allurereports/  SeleniumFramework/tests/test_contactform.py       # noqa
allure serve SeleniumFramework/reports/allurereports/
"""
import unittest
import pytest
from SeleniumFramework.pages.ContactFormPage import ContactForm
from SeleniumFramework.utilities import CustomLogger as cl


@pytest.mark.usefixtures("before_class", "before_method")
class ContactFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_objects(self):
        self.cf = ContactForm(self.driver, self.url)

    # @pytest.mark.run(order=1)
    def test_cf1_displayedform(self):
        cl.allureLogs('Web Site Opened.')
        self.cf.click_on_form_menu_option()
        self.cf.verify_form_page_is_displayed()

    # @pytest.mark.run(order=2)
    def test_cf2_fillform(self):
        self.cf.enter_name()
        self.cf.enter_email()
        self.cf.select_female_gender()
        self.cf.enter_technology()
        self.cf.enter_message()
        self.cf.enter_captcha_text()
        self.cf.submit_contact_form()
