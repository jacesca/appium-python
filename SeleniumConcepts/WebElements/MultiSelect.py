"""
Run
python -m SeleniumConcepts.WebElements.MultiSelect
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,
                                        NoSuchElementException)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
wait = WebDriverWait(
    driver=driver,
    timeout=25,
    poll_frequency=1,
    ignored_exceptions=[ElementNotVisibleException, NoSuchElementException]
)

# Open site
driver.get('http://dummypoint.com/seleniumtemplate.html')
time.sleep(2)

# Multi Select Object
########################
# <select id="multiselect" multiple="">
# <option value="mOption">mOptions</option>
# <option value="mOptionOne">mOption1</option>
# <option value="mOptionTWo">mOption2</option>
# <option value="mOptionThree">mOption3</option>
# <option value="mOptionFour">mOption4</option>
# <option value="mOptionFive">mOption5</option>
# </select>
########################
element = wait.until(EC.presence_of_element_located((By.ID, "multiselect")))
select_obj = Select(element)
print("Is multiselct?", select_obj.is_multiple)   # True

# List the values in DropDown Menu
for dd_value in select_obj.options:
    print(f"Value: {dd_value.get_property('value')}, Text: {dd_value.text}")
time.sleep(2)

# Click by index
select_obj.select_by_index(1)  # Option1
time.sleep(2)

# Click by value
select_obj.select_by_value('mOptionThree')
time.sleep(2)

# Click by text
select_obj.select_by_visible_text('mOption5')

# Select all
for option in select_obj.options:
    if not option.is_selected():
        option.click()
time.sleep(2)

# Deselect by index
select_obj.deselect_by_index(1)
time.sleep(2)

# Deselect by value
select_obj.deselect_by_value('mOptionThree')
time.sleep(2)

# Deselect by text
select_obj.deselect_by_visible_text('mOption5')
time.sleep(2)

# Deselect all
select_obj.deselect_all()
time.sleep(2)

# Close driver
time.sleep(5)
driver.quit()
