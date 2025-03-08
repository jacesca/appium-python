from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/sujithreddy/Documents/Others/Drivers/chromedriver")  # Using Chrome Driver

driver.get("http://www.dummypoint.com/Frame.html")
assert "Selenium Template" in driver.title

wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

ele = driver.find_elements(By.TAG_NAME, "iframe")

# To display number of Iframes in web page
print("List of iframe : ", len(ele))

""" 
# Switch to iframe by index
time.sleep(2)
driver.switch_to.frame(1)

data = driver.find_element(By.ID,"framename")
print("Frame Name is : ",data.text) """

"""  
# Switch to iframe by name
time.sleep(2)
driver.switch_to.frame("farme3")

data = driver.find_element(By.ID,"framename")
print("Frame Name is : ",data.text)  """


"""   
# Switch to iframe by id
time.sleep(2)
driver.switch_to.frame("f4")

data = driver.find_element(By.ID,"framename")
print("Frame Name is : ",data.text) """


# Switch to iframe by WebElement

time.sleep(2)
ele = driver.find_element(By.ID,"f2")
driver.switch_to.frame(ele)

data = driver.find_element(By.ID,"framename")
print("Frame Name is : ",data.text)


# Switching back to normal content page from frame
time.sleep(2)
driver.switch_to.default_content()

data = driver.find_element(By.ID,"framename")
print("Webpage Name is : ",data.text)

time.sleep(2)
driver.quit()