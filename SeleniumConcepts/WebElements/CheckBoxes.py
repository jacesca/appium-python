"""
Run
python -m SeleniumConcepts.WebElements.CheckBoxes
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('http://dummypoint.com/seleniumtemplate.html')
time.sleep(2)

# Check Boxes Btns
########################
# <input type="checkbox" name="checkbox" value="c1">
# <input type="checkbox" name="checkbox" value="c2">
# <input type="checkbox" name="checkbox" value="c3">
########################

# Find the list of elements
check_boxes = driver.find_elements(By.NAME, "checkbox")

# Navigate through found elements
for elem in check_boxes:
    check_boxes_value = elem.get_attribute('value')
    if check_boxes_value == 'c3':
        elem.click()
    else:  # Unselect the rest
        if elem.is_selected():
            elem.click()

for elem in check_boxes:
    print(check_boxes_value, "Is selected?", elem.is_selected())

time.sleep(5)
driver.quit()
