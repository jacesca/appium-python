import unittest
import pytest
import time
from SeleniumFrameWork.pages.EnterTextPage import EnterText

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class EnterTextTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.et = EnterText(self.driver)

    @pytest.mark.run(order=4)
    def test_enterDataInEditBox(self):
        self.driver.maximize_window()
        time.sleep(2)
        self.et.enterText()
        self.et.clickOnSubmitButton()

    @pytest.mark.run(order=3)
    def test_clickOnLocatorsPage(self):
        self.et.clickOnLocatorsPage()