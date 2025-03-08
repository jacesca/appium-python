"""
Test cases:
- Open Contact Form
- Fill & Submit Contact Form

Run
`$ pytest -v -s AppiumFramework/tests/ContactUsFormTest.py`

With Allure Reports
`$ pytest -v -s --alluredir AppiumFramework/reports/allurereports/  AppiumFramework/tests/ContactUsFormTest.py`   # noqa
`$ allure serve AppiumFramework/reports/allurereports/

"""

import unittest
import pytest
from AppiumFramework.pages.ContactUsFormPage import ContactUsForm
from AppiumFramework.utilities import CustomLogger as cl


@pytest.mark.usefixtures("before_class", "before_method")
class ContactFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_objects(self):
        self.cf = ContactUsForm(self.driver)

    # @pytest.mark.run(order=1)
    def test_contact1_open_form(self):
        cl.allureLogs('App launched.')
        self.cf.click_contact_form()
        self.cf.verify_contact_page()

    # @pytest.mark.run(order=2)
    def test_contact2_fill_form(self):
        self.cf.send_name()
        self.cf.send_email()
        self.cf.send_address()
        self.cf.send_mobile()
        self.cf.submit_contact_form()
