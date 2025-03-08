import unittest
import pytest
import time
from SeleniumFrameWork.base.BasePage import BaseClass
from SeleniumFrameWork.pages.ContctFormPage import ContactForm
import SeleniumFrameWork.utilities.CustomLogger as cl

@pytest.mark.usefixtures("beforeClass","beforeMethod")
class ContactFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = ContactForm(self.driver)
        self.bp = BaseClass(self.driver)


    @pytest.mark.run(order=2)
    def test_enterDataInForm(self):
        time.sleep(5)
        self.cf.enterName()
        self.cf.enterEmail()
        self.cf.enterMessage()
        self.cf.enterCaptha()
        self.cf.clickOnPostButton()

    @pytest.mark.run(order=1)
    def test_formPage(self):
        self.cf.clickContactForm()
        self.cf.verifyFormPage()
