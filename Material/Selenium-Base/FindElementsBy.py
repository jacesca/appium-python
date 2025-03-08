from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/Users/sujithreddy/Documents/Code2Lead/drivers/chromedriver")

driver.get("http://www.dummypoint.com/seleniumtemplate.html")
time.sleep(2)

ele = driver.find_elements(By.ID,"menu")

for menu in ele:
    print(menu.text)

time.sleep(5)
driver.quit()