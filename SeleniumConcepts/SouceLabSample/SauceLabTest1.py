"""
Run
python -m SeleniumConcepts.SouceLabSample.SauceLabTest1
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,
                                        NoSuchElementException)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions


usr_nam = "oauth-jacesca-e66ae"
acc_key = "d88ca88f-2e9c-4cd6-b676-12c9b0886f0a"

options = ChromeOptions()
options.browser_version = 'latest'
options.platform_name = 'macOS 13'

sauce_options = {}
sauce_options['username'] = usr_nam
sauce_options['accessKey'] = acc_key
sauce_options['build'] = '2024'
sauce_options['name'] = 'TestAutomationExample'

options.set_capability('sauce:options', sauce_options)

url = f"https://ondemand.us-west-1.saucelabs.com:443/wd/hub"    # noqa
driver = webdriver.Remote(
    command_executor=url,
    options=options,
    keep_alive=True
)

# run commands and assertions
driver.get('http://dummypoint.com/seleniumtemplate.html')
time.sleep(2)

wait = WebDriverWait(
    driver=driver,
    timeout=25,
    poll_frequency=1,
    ignored_exceptions=[ElementNotVisibleException, NoSuchElementException]
)
element = wait.until(EC.presence_of_element_located((By.ID, "user_input")))
element.send_keys('Code2Lead')

time.sleep(5)

title = driver.title
titleIsCorrect = "Selenium Template — DummyPoint" in title
jobStatus = "passed" if titleIsCorrect else "failed"

# end the session
driver.execute_script("sauce:job-result=" + jobStatus)
driver.quit()
