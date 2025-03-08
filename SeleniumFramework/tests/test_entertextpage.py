"""Run
pytest -v -s SeleniumFramework/tests/test_entertextpage.py

With Allure Reports
pytest -v -s --alluredir SeleniumFramework/reports/allurereports/  SeleniumFramework/tests/test_entertextpage.py       # noqa
allure serve SeleniumFramework/reports/allurereports/
"""
import unittest
import pytest
import time
from SeleniumFramework.pages.EnterTextPage import EnterTextPage
from SeleniumFramework.utilities import CustomLogger as cl


@pytest.mark.usefixtures("before_class", "before_method")
class EnterTextTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_objects(self):
        self.et = EnterTextPage(self.driver, self.url)

    # @pytest.mark.run(order=1)
    def test_enter1_click_on_locator_page(self):
        cl.allureLogs('Web Site Opened.')
        self.et.click_on_locator_menu_option()

    # @pytest.mark.run(order=2)
    def test_enter2_submit_entered_text(self):
        self.et.driver.maximize_window()
        time.sleep(2)
        self.et.enter_text()
        self.et.submit_enter_text_form()
