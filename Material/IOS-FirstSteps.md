# IOS Config

# Open project
- Open Folder `/Users/j.escalante/Documents/Courses/Appium-Python/Apps/ios-uicatalog-master/UIKitCatalog`
- DoubleClick on `UIKitCatalog.xcodeproj`
- Project will be open en XCode


# To run the app in the emulated device:
- After complete previous steps (`open project`)
- Look for `UIKitCatalog.app` in subfolder `Product`
- Copy file into a known location

# To run app in XCode
- After completed steps from `open project`
- Select app 
- In bar menu select device to test
- Click on run

# Errors

1. To solve `Appium Error: Could not get Xcode version`. Run
    ```
    sudo xcode-select --switch /Applications/Xcode.app
    ```
    [More...](https://stackoverflow.com/questions/32724616/appium-error-could-not-get-xcode-version)

2. To solve `Unable to launch WebDriverAgent because of xcodebuild failure: xcodebuild failed with code 65`. 
    > Ensure no cisco vpn is active.

3. To solve `OS Inspector won't load`
Run
    `appium driver update xcuitest --unsafe`

    If the previous did not resolve the problem, do the following in XCode:
    - Go to project that gives you the problem
    - Menu Product >> Clean Build Folder
    - Menu Product >> Build

    [More](https://stackoverflow.com/questions/44159951/unable-to-launch-webdriveragent-because-of-xcodebuild-failure-xcodebuild-failed)



# Util commands
1. List virtuaal devices `xcrun simctl list devices`
2. List app installed `xcrun simctl listapps {DEVICE_UUID}`, p.e. `xcrun simctl listapps 2535D1C9-4E10-483C-8126-3D7B5722E499`
