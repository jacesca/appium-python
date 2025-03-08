## Commands to find details


`$ adb devices` >> usb device connected to get the udid
`$ adb shell dumpsys window windows` >> to find the app package name (app needs to be 
                                        open). 
                                        Review output.txt for more details.
                                        Look for last window (in this example: window 21) and look for:
                                        imeLayeringTarget in display# 0 
                                            Window{ee6e09b u0 com.code2lead.kwad/com.code2lead.kwad.MainActivity}
                                        imeInputTarget in display# 0 
                                            Window{ee6e09b u0 com.code2lead.kwad/com.code2lead.kwad.MainActivity}
                                        imeControlTarget in display# 0 
                                            Window{ee6e09b u0 com.code2lead.kwad/com.code2lead.kwad.MainActivity}
`adb shell dumpsys window windows | grep imeLayeringTarget`

## Desired Capabilities 

Desired Capabilities are keys and values encoded in a JSON object, sent by Appium clients to the server when a new automation session is requested. 
 
desired_caps = {} 
desired_caps['platformName'] = 'Android' 
desired_caps['platformVersion'] = '14' 
desired_caps['deviceName'] = 'Galaxy S23' 
desired_caps['app'] = ('/Documents/Code2Lead/Android_Demo_App.apk') 
desired_caps['appPackage'] = 'com.code2lead.kwad' 
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity' 


## Appium Inspector values:

{
  "automationName": "uiautomator2",
  "appPackage": "com.code2lead.kwad",
  "appActivity": "com.code2lead.kwad.MainActivity",
  "platformName": "Android",
  "deviceName": "Galaxy S23",
  "udid": "RFCXA08HHRA",
  "newCommandTimeout": 600
}


# Hybrid apps
Prerequisites:
- Mobile Browser and ChromeDriver must be in same version
    - Mobile brower: open chrome >> settings >> about >> version
    - ChromeDriver: open terminal >> chromedriver --version
    If version are not equal, you can download it from:
        https://chromedriver.chromium.org/
    To install in Mac:
        $ brew uninstall chromedriver
        $ brew install chromedriver
        $ where chromedriver
        $ cd /opt/homebrew/bin/chromedriver   # or wherever is chromedriver
        $ xattr -d com.apple.quarantine chromedriver
        $ chromedriver --version
- Locators should be identified in web properly:
    - open chrome browser and type browser://inspect/#devices
      (https://inspector.appiumpro.com)
    - use browser inspector