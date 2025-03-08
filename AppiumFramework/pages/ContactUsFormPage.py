from AppiumFramework.base.BasePage import BasePage
from AppiumFramework.utilities import CustomLogger as cl


class ContactUsForm(BasePage):
    # locators values in ContactUsForm
    _contact_form_btn_id = 'com.code2lead.kwad:id/ContactUs'   # id
    _contact_page_title_txt = 'Contact Us form'                # text
    _contact_name_txt = 'Enter Name'                           # text
    _contact_email_txt = 'Enter Email'                         # text
    _contact_address_txt = 'Enter Address'                     # text
    _contact_mobile_idx = '4'                                  # index
    _contact_submit_btn_txt = 'SUBMIT'                         # text

    def __init__(self, driver):
        super().__init__(driver)

    def click_contact_form(self):
        self.click_element(self._contact_form_btn_id)
        cl.allureLogs('Clicked on Contact Us Form Button.')

    def verify_contact_page(self):
        displayed_flag = self.is_displayed(
            self._contact_page_title_txt,
            'text'
        )
        assert displayed_flag
        cl.allureLogs('Contact Us Form Page opened.')

    def send_name(self):
        self.send_text('Code2Lead', self._contact_name_txt, 'text')
        cl.allureLogs('Entered contact name.')

    def send_email(self):
        self.send_text('Code2Lead@gmail.com', self._contact_email_txt, 'text')
        cl.allureLogs("Entered contact email.")

    def send_address(self):
        self.send_text('Road st, #523, NY', self._contact_address_txt, 'text')
        cl.allureLogs("Entered contact address.")

    def send_mobile(self):
        self.send_text('123 456 7890', self._contact_mobile_idx, 'index')
        cl.allureLogs('Entered contact mobile number.')

    def submit_contact_form(self):
        self.screenshot('contactus')
        self.click_element(self._contact_submit_btn_txt, 'text')
        cl.allureLogs('Contact Us Form Submit button clicked.')
