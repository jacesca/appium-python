"""Run
$ pytest -v -s tests/test_contactform.py

With Allure Reports
$ pytest -v -s --alluredir reports/allurereports/  tests/test_contactform.py
$ allure serve reports/allurereports/
"""

import unittest
import pytest
from pages.ContactUsFormPage import ContactUsForm
from utilities import CustomLogger as cl


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
