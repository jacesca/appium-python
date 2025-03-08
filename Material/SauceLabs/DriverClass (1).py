from appium import webdriver


class Driver:
    saucelab_username = "xxxxxx"
    saucelab_accesskey = "xxxxxx-8f43-4994-xxxx-xxxxxxxx"

    def getDriverMethod(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = 'Pixel'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['app'] = ('/Users/sujithreddy/Documents/Code2Lead/Others/Android_Appium_Demo_APK/Android_Demo_App.apk')
        desired_caps['appPackage'] = 'com.code2lead.kwad'
        desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        return driver

    def cloudDriver(self,pVersion,pName):
        caps = {}
        caps['appiumVersion'] = "1.17.1"
        caps['deviceName'] = "Google Pixel 3a XL GoogleAPI Emulator"
        caps['deviceOrientation'] = "portrait"
        caps['platformVersion'] = pVersion
        caps['platformName'] = pName
        caps['app'] = "storage:filename=Android_Demo_App.apk"
        caps['name'] = "Android Test"
        caps['build'] = "Version 1.1"
        caps['tags'] = ['v3', 'v4']
        caps['username'] = self.saucelab_username
        caps['accesskey'] = self.saucelab_accesskey

        url = "https://@ondemand.us-west-1.saucelabs.com:443/wd/hub"

        driver = webdriver.Remote(url, caps, keep_alive=True)

        return driver

