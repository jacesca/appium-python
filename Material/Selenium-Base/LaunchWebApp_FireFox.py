from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="/Users/sujithreddy/Documents/Code2Lead/drivers/geckodriver")

driver.get("http://www.dummypoint.com/seleniumtemplate.html")

time.sleep(5)
driver.quit()