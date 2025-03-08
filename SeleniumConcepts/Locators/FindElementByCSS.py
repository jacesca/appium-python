"""
Run
python -m SeleniumConcepts.Locators.FindElementByCSS

Below there are some of the ways to find WebElement by CssSelector:
1. To write id name in css selector, you need to add `#` before id value;
2. To write class name in css selector, you need to add `.` before class name;
3. Using `tag name("input")` and `name` attribute value as css_selector;
4. Using `tag name("input")`, `classname` and `name` attribute value as
   css_selector;
5. `^` - Find elements using starts with a string value;
6. `$` - Find elements using Ends with a string value;
7. `*` - Find elements using contains a substring;
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
# 1. Using ID name in css_selector
driver.find_element(By.CSS_SELECTOR, "#user_input").send_keys('CSS_SELECTOR_ID')   # noqa
# 2. Using CSS_NAME (class name attribute) in css_selector
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".entertext").send_keys('_ClassName')   # noqa# 3. Using `tag name` and `name` attribute
# 3. Using `tag name` and `name` attribute
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, 'input[name="textbox"]').send_keys('_TagName and Name')   # noqa
# 4. Using `tag name`, `classname` and `name` attribute
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, 'input.entertext[name="textbox"]').send_keys('_TagName, ClassName and Name')   # noqa
# 5. `^` - Find elements using starts with a string value
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, 'input[name^="text"]').send_keys('_^_START_NAME')   # noqa
# 6. `$` - Find elements using Ends with a string value
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, 'input[class$="text"]').send_keys('_$_END_CLASSNAME')   # noqa
# # 7. `*` - Find elements using contains a substringe
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, 'input[class*="terte"]').send_keys('_*_CONTAINS_CLASSNAME')   # noqa

time.sleep(5)
driver.quit()
