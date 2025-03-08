"""
Run
python -m SeleniumConcepts.Locators.FindElementByXPath

Below there are some of the ways to find WebElement by XPath:
1. Absolute path
    - It uses from complete html root path to the required WebElement
    - Ex. `html/body/div/div[2]/div[2]/div/div/div/div[2]/form/input[1]`
      or `//form/input[1]`
    - `/`: Find the element inside the parent element.
    - `//`: Find the child inside the parent element.
2. Relative to XPATH:
    - It uses the direct path of an element using (id, className, attribute
      values). Ex
        - `//*[@id='user_input']` or `//input[@id='user_input']`
    - Using contains:
        - Sintax `//tag[contains(@attribute , 'partial value')]`
        - Ex. `//input[contains(@id, 'user')]` or
          `//a[contains(text(), 'Form')]`
    - Using starts with:
        - Sintax `//tag[starts-with(@attribute, 'first part value')]`
        - Ex. `//input[starts-with(@id, 'user')]`
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('http://dummypoint.com/seleniumtemplate.html')
time.sleep(2)

#########################################################################
# <input type="text" name="textbox" id="user_input" class="entertext">
#########################################################################
# 1. By Full XPATH
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/section/div[2]/div/form/input[1]").send_keys('XPATH_FULL')   # noqa
# 2. By Relative XPATH
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="user_input"]').send_keys('_XPATH_RELATIVE')   # noqa# 3. Using `tag name` and `name` attribute
# 3. By Relative XPATH using attribute
time.sleep(2)
driver.find_element(By.XPATH, '//*[@class="entertext"]').send_keys('_XPATH_ATTRIBUTE_CLASS')   # noqa# 3. Using `tag name` and `name` attribute
# 4. By Relative XPATH using attribute and Contains
time.sleep(2)
driver.find_element(By.XPATH, '//input[contains(@class, "terte")]').send_keys('_CONTAINS')   # noqa# 3. Using `tag name` and `name` attribute
# 5. By Relative XPATH using attribute and Starts-With
time.sleep(2)
driver.find_element(By.XPATH, '//input[starts-with(@class, "enter")]').send_keys('_STARTS-WITH')   # noqa# 3. Using `tag name` and `name` attribute

time.sleep(5)
driver.quit()
