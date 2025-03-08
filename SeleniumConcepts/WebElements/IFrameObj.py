"""
Run
python -m SeleniumConcepts.WebElements.IFrameObj
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,
                                        NoSuchElementException)
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
wait = WebDriverWait(
    driver=driver,
    timeout=25,
    poll_frequency=1,
    ignored_exceptions=[ElementNotVisibleException, NoSuchElementException]
)

# Open site
driver.get('http://dummypoint.com/Frame.html')
time.sleep(2)

# IFrame Object
########################
# <div class="card-body">
# <!--Frame start -->
# <iframe name="farme1" id="f1" src="frame_1.html"></iframe>
# <iframe name="farme2" id="f2" src="frame_2.html"></iframe><br><br>
# <iframe name="farme3" id="f3" src="frame_3.html"></iframe>
# <iframe name="farme4" id="f4" src="frame_4.html"></iframe>
# <h1 id="framename">Content Page</h1>
# <button name="promtalert" onclick="myFunction()">Promt Alert</button>
# <p id="demo"></p>
# <!--Frame End -->
# </div>
########################
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "card-body")))

# Find all iframes
elements = driver.find_elements(By.TAG_NAME, 'iframe')
print("Total IFrames found            :", len(elements))
frame_element = driver.find_element(By.ID, 'framename')
print('Current title  (ParentFrame)   :', frame_element.text)
time.sleep(2)

# Switch to iframe by id
driver.switch_to.frame('f1')       # frame1
frame_element = driver.find_element(By.ID, 'framename')
print('Title on Frame (id=f1)         :', frame_element.text)
time.sleep(2)

# Switch to iframe by index
driver.switch_to.parent_frame()    # return to parent
driver.switch_to.frame(1)          # frame2
frame_element = driver.find_element(By.ID, 'framename')
print('Title on Frame (Index 1)       :', frame_element.text)
time.sleep(2)

# Switch to iframe by name
driver.switch_to.parent_frame()    # return to parent
driver.switch_to.frame('farme3')   # frame3
frame_element = driver.find_element(By.ID, 'framename')
print('Title on Frame (name=farme3)   :', frame_element.text)
time.sleep(2)

# Switch to iframe by web element
driver.switch_to.parent_frame()    # return to parent
iframe_element = driver.find_element(By.ID, 'f4')
driver.switch_to.frame(iframe_element)   # frame4
frame_element = driver.find_element(By.ID, 'framename')
print('Title on Frame (with web elem) :', frame_element.text)

# Return to parent
driver.switch_to.default_content()
print('Returning to Parent Frame Again')
frame_element = driver.find_element(By.ID, 'framename')
print('Current title  (ParentFrame)   :', frame_element.text)

# Close driver
time.sleep(5)
driver.quit()
