from selenium import webdriver
import time

from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec

driver = webdriver.Chrome("/Users/sujithreddy/Documents/Code2Lead/drivers/chromedriver")

driver.get("http://www.dummypoint.com/seleniumtemplate.html")
assert "Selenium Template" in driver.title
time.sleep(2)

wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])
wait.until(ec.presence_of_element_located((By.LINK_TEXT,"FORM"))).click()
wait.until(ec.presence_of_element_located((By.ID,"reused_form")))
time.sleep(2)

wait.until(ec.presence_of_element_located((By.ID,"name"))).send_keys("Code2Lead")
wait.until(ec.presence_of_element_located((By.ID,"email"))).send_keys("abc@gmail.com")
wait.until(ec.presence_of_element_located((By.ID,"message"))).send_keys("ABCDEFG")
captcha = wait.until(ec.presence_of_element_located((By.ID,"captcha_image")))
wait.until(ec.presence_of_element_located((By.ID,"captcha"))).send_keys(captcha.text)

postButton = wait.until(ec.presence_of_element_located((By.ID,"btnContactUs")))

# Scroll Gesture
actions = ActionChains(driver)
actions.move_to_element(postButton).perform()
postButton.click()

time.sleep(5)
driver.quit()