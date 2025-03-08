"""
Run
python -m SeleniumConcepts.WebElements.RadioBtn
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('http://dummypoint.com/seleniumtemplate.html')
time.sleep(2)

# Radio Btns
########################
# <input type="radio" name="radio" value="Button1">
# <input type="radio" name="radio" value="Button2">
# <input type="radio" name="radio" value="Button3">
# <input type="radio" name="radio" value="Button4">
########################

# Find the list of elements
radio_btns = driver.find_elements(By.NAME, "radio")

# Navigate through found elements
for elem in radio_btns:
    radio_btn_value = elem.get_attribute('value')
    if radio_btn_value == 'Button4':
        elem.click()

for elem in radio_btns:
    print(radio_btn_value, "Is selected?", elem.is_selected())

time.sleep(5)
driver.quit()
