from SeleniumFrameWork.base.BasePage import BaseClass
import SeleniumFrameWork.utilities.CustomLogger as cl

class ContactForm(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators  values in Contact form page

    _contactFromPage = "FORM"  # link
    _formPage = "reused_form"  # id
    _enterName = "name"  # id
    _enterEmail = "emai"  # id
    _enterMessage = "message"  # id
    _getCaptcha = "captcha_image"  # id
    _enterCaptha = "captcha"  # id
    _postButton = "btnContactUs"  # id

    def clickContactForm(self):
        self.clickOnElement(self._contactFromPage, "link")

    def verifyFormPage(self):
        element = self.isElementDisplayed(self._formPage, "id")
        assert element == True

    def enterName(self):
        self.sendText("Code2Lead", self._enterName, "id")

    def enterEmail(self):
        self.sendText("abc@gmail.com", self._enterEmail, "id")

    def enterMessage(self):
        self.sendText("This is a Code2Lead", self._enterMessage, "id")

    def getCaptha(self):
        cap = self.getText(self._getCaptcha, "id")
        return cap

    def enterCaptha(self):
        self.sendText(self.getCaptha(), self._enterCaptha, "id")

    def clickOnPostButton(self):
        self.scrollTo(self._postButton, "id")
        self.clickOnElement(self._postButton, "id")
