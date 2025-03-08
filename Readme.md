# Goal
Run automations on mobiles.

# Execution command
Example
```
python -m AppiumConcepts.LaunchMultipleApps.LaunchMultiApp
python -m LoggingConcepts.loggingPy.LoggingDemo.py
pytest -n auto PyTestConcepts.pytest_parallel
```

# Automations availables
For Android devices:
    - AndroidDrivers
    - basics
    - ElementActions
    - ElementProperties
    - gestures
    - hybrid
    - locators
    - ResetStrategies
    - Waits
For IOS devices:
    - IosAutomation

# Hybrid apps - WebView
Run `{browser}://inspect/#devices`
p.e. in chrome:
```
chrome://inspect/#devices
```

# to run any automation
`python -m <foder/module name>.<python file name without extension>
> Example:
> `python -m basics.GalaxyLaunchApp`

# Find Main Activity of a package in device
```
adb shell pm list packages | grep telus         # List pkgs
adb shell pm dump com.telus.myaccount.dev | grep -A 1 MAIN      # List main activities
```

# How to Find Package Name and Activity Name of an Application (old)
[Source](https://medium.com/huawei-developers/how-to-find-package-name-and-activity-name-of-an-application-0b6858ec4f5d)

## First method
1. Open the app in the connected device
2. Run
```
$ adb devices
$ adb shell
    dm1q:/ $ dumpsys window displays | grep -E "mCurrentFocus"

    mCurrentFocus=null
    mCurrentFocus=Window{f1f80ed u0 com.android.vending/com.android.vending.AssetBrowserActivity}
```

## Second method
```
$ adb shell dumpsys window windows | grep imeLayeringTarget
  imeLayeringTarget in display# 0 Window{9364929 u0 com.android.vending/com.android.vending.AssetBrowserActivity}
```

# Developer mode in phone
- 7 double click on build number, locater in settings>>about phone>sw information>>build number
- A pop up telling that developer mode is now activated will appear.
- Go back and at the same level of about phone, a new option will appears “developer options”
- Toggle on usb debugging
- Toggle on pointer location


# Instalation of allure reports
```
pip install allure-pytest
brew install allure
```
Then update the $path variable
```
open ~/.zshrc  
```
and add `export PATH="/opt/homebrew/opt/allure/bin:$PATH"`

# How to recover the apk from Android
```
adb shell pm list packages | grep telus
adb shell pm path com.telus.myaccount
adb pull /data/app/~~aHsb5YrjVeaiKULpAmze6Q==/com.telus.myaccount-OXam2EiFYj7xDu3l3KZxkQ==/base.apk
```

# To keep standard codification
- Innstall Flake8 plugin in VSCode
- Add flake8 and black to environment
```
pip install black
pip install flake8
```
Then you can run
```
black model.py
flake8 model.py
```

# Other documentation
- [Android Key Codes](https://stackoverflow.com/questions/7789826/adb-shell-input-events)
- [Send return key for iOS Appium python](https://stackoverflow.com/questions/54877107/send-return-key-for-ios-appium-python)
- [Appium Mobile Driver Desired Capabilities](https://appium.github.io/appium.io/docs/en/writing-running-appium/caps/)
- [selenium.common.exceptions](https://www.selenium.dev/selenium/docs/api/py/common/selenium.common.exceptions.html)
- [selenium.webdriver.support.expected_conditions](https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html)
- [Behave Documentation Tutorial](https://behave.readthedocs.io/en/stable/tutorial.html#)
- [Allow or deny all permissions for iOS apps](https://www.browserstack.com/docs/app-automate/appium/advanced-features/handle-permission-pop-ups)

# Related errors in selenium
- [Unable to use Selenium Webdriver. Getting two exceptions](https://stackoverflow.com/questions/76461596/unable-to-use-selenium-webdriver-getting-two-exceptions)
    > If the Selenium version you are using is v4.6.0 or above, then you don't really have to set the driver.exe path. Selenium can handle the browser and drivers by itself. (Current selenium==4.15.2)
- [Could not create a session: You must enable 'Allow remote automation' in the Developer section of Safari Settings to control Safari via WebDriver.](https://stackoverflow.com/questions/41629592/macos-sierra-how-to-enable-allow-remote-automation-using-command-line)
    > On MacBook Pro (Apple M2 Pro) ▪ select Safari ▪ Select Setting ▪ Select “Advanced” tab ▪ Check “Show features for web developers” ▪ Now you see “develop” option is on the MacOS menu ⁃ select develop ⁃ Select “Developer settings…” ⁃ check “Allow remote automation” Now you can run your tests against safari

# Firefox instalation
- Look for `firefox`, `geckodriver` in [homebrew](https://brew.sh/) page.
- Run `brew install --cask firefox`
- Runn `brew install geckodriver`

# BDD
```
pip install behave
pip install allure-behave
```

# To run allure reports
Generate reports
```
behave -f allure_behave.formatter.AllureFormatter -o %allure_result_folder% ./features
allure serve "logs_path"
```

# Installing jenkins
    ```
    brew install jenkins
    ```
Output:
    ```
    Caveats
    Note: When using launchctl the port will be 8080.

    To start jenkins now and restart at login:
    brew services start jenkins
    Or, if you don't want/need a background service you can just run:
    /opt/homebrew/opt/jenkins/bin/jenkins --httpListenAddress\=127.0.0.1 --httpPort\=8080
    ==> Summary
    🍺  /opt/homebrew/Cellar/jenkins/2.491: 9 files, 95.6MB
    ==> Running `brew cleanup jenkins`...
    Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
    Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
    ==> Caveats
    ==> jenkins
    Note: When using launchctl the port will be 8080.

    To start jenkins now and restart at login:
    brew services start jenkins
    Or, if you don't want/need a background service you can just run:
    /opt/homebrew/opt/jenkins/bin/jenkins --httpListenAddress\=127.0.0.1 --httpPort\=8080
    ```

To start jenkins now and restart at login:
    ```
    brew services start jenkins
    ```

Or, if you don't want/need a background service you can just run:
    ```
    /opt/homebrew/opt/jenkins/bin/jenkins --httpListenAddress\=127.0.0.1 --httpPort\=8080
    ```

## To find where is jenkins
    ```
    where jenkins
    ```

## To review jenkins version
    ```
    jenkins --version
    ```

## To access Jenkins Logs files:
    ```
    /opt/homebrew/var/log/jenkins
    ```

## Jenkins Conf file
    ```
    /Users/j.escalante/.jenkins/secrets/initialAdminPassword
    ```

## Quick guide to start using Jenkins (once installed):
- Prerrequisites
    - Full Access on Terminal
        - Settings >> Privacy & Security >> Full Disk Access >> Terminal Toggled On
- New Item
- Named `PythonTestAutomation`
- Select `FreeStyle Project`
- Click `Ok` Btn
- Click on `Advance` Btn
- Scroll down and click on `Use Custom Workspace` checkbox
- Set the directory path to the project (SeleniumFramework): 
  `/Users/j.escalante/Documents/Courses/Appium-Python`
- Scroll down until `Build` section
- Click on `Add build step` dropdown menu
- Select `Execute Shell` option
- Enter the command to execute: 
    ```
    source /Users/j.escalante/.zshrc
    conda activate appium
    pytest -v -s --alluredir SeleniumFramework/reports/allurereports/  SeleniumFramework/tests/TestSuitRegression.py
    ```
- Click on `Save` btn
- Click on `Build Now` menu option (left menu)

## Configure Scheduler to created Automation
- Enter to http://localhost:8080/
- Select the automation
- Click on `Configuration` (left menu)
- Scroll until `Trigger` Section
- Click on `Build periodically` checkbox
- Add the cronjob schedule, ex. `H 9 * * 1-5` (at 9:00am from Monday to Friday)
- Click on `Apply` and `Save` btns.


# SauceLab

Site: https://app.saucelabs.com/
Documentation: [sauce:visual Capability Options](https://docs.saucelabs.com/visual/e2e-testing/commands-options/#saucevisual-capability-options)

Steps:
1. Create account
2. Go to user settings, scroll until Get Access key and save it with the user name and ondemand url. From the url, we need to remove user and pwd as they are configured apart.
3. Review browsee supported
    - Go to https://saucelabs.com/
    - Menu Products >> Supported Browser & Devices
    - Scroll until `>> See Platform Configurator <<` btn
    - Click on it
    - Play with the desired configuration, MAC-CHROME-PYTHON-SELENIUM 4
    - Copy sample configuration to apply to your automation
4. Run locally the adapted file
    `python -m SeleniumConcepts.SouceLabSample.SauceLabTest1`
5. Go to https://app.saucelabs.com/ >> Automated >> Test Results

# Some appium (python code)
## Scroll until element
```
TouchAction().press(el0).moveTo(el1).release()
```

# Commands for ios
List the devices >> `xcrun simctl list`
List the active devices >> `xcrun simctl list | grep Booted`
List all of the installed applications on the Simulator 
    `xcrun simctl listapps {DEVICE_UUID} | grep myapp`  # com.myapp.myaccount
uninstall an app:
    `xcrun simctl uninstall booted com.myapp.myaccount`

# How to get the udid in iphone devices
Run 
```
xcrun xctrace list devices
```
Output expected:
```
== Devices ==
MBSVLCDISHPH65T (1F3E8F96-94B7-5203-A0FB-493767537E4E)
Jacqueline Escalante’s iPhone (18.2.1) (00008120-001969A03AC2601E)

== Simulators ==
Apple Watch SE (40mm) (2nd generation) Simulator (11.2) (38157A4D-1A61-474B-BF2C-6F836814FC89)
Apple Watch SE (44mm) (2nd generation) Simulator (11.2) (1514E11E-9170-4790-990C-7F04AB919F1E)
...
```

For device, udid = 00008120-001969A03AC2601E

# To get the app from xcode
On the bar icon on the left side, click on the last icon related to build log
The log will appear, and copy the path showed there
```
/Users/j.escalante/Library/Developer/Xcode/DerivedData/UIKitCatalog-gpjtxvrioqhghccuvfvxwtwwizdc/Build/Products/Debug-iphoneos/UIKitCatalog.app
```

# Preventing blocked by Safari issues do not Work
Source: 
> https://stackoverflow.com/questions/33790957/unable-to-click-on-a-button-link-on-mobile-view-ios-via-appium-using-capybara
Problem: 
> Click button does not open the window because Safari blocked it
Solution:
> Change configuration in Safari.
Steps:
> - Go to iphone settings
> - Under general part, turn off "Block pop-ups"

# Get UUID
From android: 
`adb shell 'settings get secure android_id'`
`adb -s <YOUR-DEVICE-ID> shell getprop` # device id is got from `adb devices`

From iOS:
1. Initiate iTunes/Music and connect your device.
2. Go to Devices and select your device by clicking on it.
3. Click on 'serial number.
4. Your 'serial number' will automatically change to your UDID.
5. Click on the 'Edit' icon, then 'Copy' 
6. ‘Paste’ the same (taken from iTunes menu) into your email. The email message will display your UDID.