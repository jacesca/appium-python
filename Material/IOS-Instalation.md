# IOS Automation With Appium Using Python

1. Download the Xcode and install it from “App Store”
2. Download the Appium IOS App Demo code (.zip file) from gitgub 
    - Google it for “UI Catalog”
    - Open the github link  https://github.com/appium/ios-uicatalog 

3. UnZip the file and click on click on UICatalog folder and then click on UICatalog.xcodeproj file in that unzip folder and it will open in xcode
4. Click on "show project navigator" @ top left under the Red cross mark in xcode
5. Under Products folder we can see the ".app" file install it in the iphone simulator and then copy the file and place it under any folder to give that path in our Appium code
6. Start the coding in IDE for Appium 


# Appium Inspector Data
```
  "platformName": "IOS",
  "platformVersion": "13.2",
  "deviceName": "iPhone 11 Pro",
  "automationName": "XCUITest",
  "app": "/Users/sujithreddy/Documents/IOS_APPS/UICatalog.app"
```

# IOS Real Device SetUp

http://appium.io/docs/en/drivers/ios-xcuitest-real-devices/

1. Install libimobiledevice and ios-deploy below brew commands
```
brew install libimobiledevice

brew install  ios-deploy
```
2. Create the Apple id (https://developer.apple.com/account/) and get the developer account you need to pay $99 (For Developer Account)
3. Open the UICatalog project( https://github.com/appium/ios-uicatalog )  in Xcode → in “General” selection  select target device version and Select ( Signing & Certificates) → select the Team ID → Give the data in “Bundle Identifier” name its is Unique name should be given
4. Select the device at top and Run it , then it will successfully install the app in your device and copy the app in some folder 
5. Now We need to create a dummy project and name it as  “WebDriverAgentRunner” and install that as well in real device “http://appium.io/docs/en/drivers/ios-xcuitest-real-devices/”
6. Create the file in Pycharm with required capabilities and execute the code

## 3.1 How to add developer id to project
> In Xcode, after opening the project (UIKitCatalog.xcodeproj)
> - Ensure you clicked in the parent folder (UKitCatalog)
> - Click on General and review data
> - Click on Signing & Capabilities
> - Add a developer id and select it in the team option
> - Give a unique bundle identifier (com.testapp.jacesca)
>

## 3.2 How to enable developer mode in iOS
> Ensure development mode is enable in device
> - Click on settings >> Privacy & security >> Enable developer mode
>

## 3.3 How to run the app in real device
> On Xcode, select the device (real device from list) and run on execution bar, if it is not working, you can clean the project and try again
>

## 3.4 How to make the app trustable to run it
> You will get a message in your device, that the source is untrusted, so
> - Go to settings >> General >> VPN & Device Management >> Look for your development id >> Make it trustable.
>

## 5.1 To deal with appium and real devices
1. Open XCode
2. Click on file >> new >> project
3. Select iOS >> App
4. Click on next
5. Fill the form
  - Product name: WebDriverAgentRunner
  - Team: select the developer id
  - Organization name: jacesca
  - Interface: SwiftUI
  - Language: Swift
6. Click on next
7. Select the path (courses>appium python>app>webdriverproject) and don't add to any proj.
8. Click on create
9. Once open click on parent folder (WebDriverAgentRunner)
10. Click on general and ensure ios version commit with the real device
11. Click on signing and confirm developer id is added and also the bundle identifier.
12. On bar select real device and run it
13. The webdriverproject will be created in the device

# IOS Hybrid App Automation

http://appium.io/docs/en/writing-running-appium/web/hybrid/

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
