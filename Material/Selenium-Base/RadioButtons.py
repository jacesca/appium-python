from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/Users/sujithreddy/Documents/Code2Lead/drivers/chromedriver")

driver.get("http://www.dummypoint.com/seleniumtemplate.html")
time.sleep(2)

# 1. find the list of radio buttons using locator
ele_r = driver.find_elements(By.NAME,"radio")
time.sleep(2)

# 2. Using for loop iterate the list object and click on required option
for rbutton in ele_r:
    rbutton_t = rbutton.get_attribute("value")
    print(rbutton_t)
    if rbutton_t == "Button2":
        rbutton.click()
        print("Is Selected : ",rbutton.is_selected())
        break



time.sleep(2)
driver.quit()