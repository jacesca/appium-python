"""
Run
python -m SeleniumConcepts.WebElements.DropDown
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

# Drop Down Menu
########################
# <select id="dropdown">
# <option value="Option">Options</option>
# <option value="OptionOne">Option1</option>
# <option value="OptionTWo">Option2</option>
# <option value="OptionThree">Option3</option>
# <option value="OptionFour">Option4</option>
# <option value="OptionFive">Option5</option>
# </select>
########################
element = wait.until(EC.presence_of_element_located((By.ID, "dropdown")))
select_obj = Select(element)
print("Is multiselct?", select_obj.is_multiple)  # None

# List the values in DropDown Menu
for dd_value in select_obj.options:
    print(f"Value: {dd_value.get_property('value')}, Text: {dd_value.text}")
time.sleep(2)

# Click by index
select_obj.select_by_index(2)  # Option2
time.sleep(2)

# Click by value
select_obj.select_by_value('OptionFive')
time.sleep(2)

# Click by text
select_obj.select_by_visible_text('Option3')

time.sleep(5)
driver.quit()
