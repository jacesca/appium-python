from selenium import webdriver
import SeleniumFrameWork.utilities.CustomLogger as cl

class WebDrivenClass:
    log = cl.customLogger()

    def getWebDriver(self, browserName):
        driver = None
        if browserName == "chrome":
            driver = webdriver.Chrome("/Users/sujithreddy/Documents/Code2Lead/drivers/chromedriver")
            self.log.info("Chrome Driver is initializing")
        elif browserName == "safari":
            driver = webdriver.Safari()
            self.log.info("Safari Driver is initializing")
        elif browserName == "firefox":
            driver = webdriver.Firefox(executable_path="/Users/sujithreddy/Documents/Code2Lead/drivers/geckodriver")
            self.log.info("FireFox Driver is initializing")

        return driver
