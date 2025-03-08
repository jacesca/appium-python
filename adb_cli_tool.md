# adb command

## List devices
```
$ adb devices
output:
    List of devices attached
    RFCXA08HHRA	device
```
> RFCXA08HHRA is the id/serial phone number, located in settings >> about phone >> {look for the serial number}

## Enter into the device
```
$ adb shell
    dm1q:/ $ ls
    output:
        acct                efs                prism
        apex                etc                proc
        audit_filter_table  init               product
        bin                 init.container.rc  sdcard
        bugreports          init.environ.rc    second_stage_resources
        cache               linkerconfig       sepolicy_version
        carrier             metadata           storage
        config              mnt                sys
        d                   odm                system
        data                odm_dlkm           system_dlkm
        data_mirror         oem                system_ext
        debug_ramdisk       omr                vendor
        dev                 optics             vendor_dlkm
        dpolicy_system      postinstall
    
    dm1q:/ $ cd storage
    
    dm1q:/storage $ ls
    output:
        emulated  self
    
    dm1q:/storage $ ls -l
    output:
        total 3
        drwxrwx--- 4 media_rw media_rw 3452 2024-08-27 19:45 emulated
        drwxr-xr-x 2 root     root       60 2024-12-20 14:00 self

    dm1q:/storage $ ls -a
    output:
        .  ..  emulated  self

    dm1q:/storage $ exit
```
> `ls` list all files contained into the device

## How to install the app with adb command
```
$ adb install /Users/j.escalante/Documents/Courses/Appium-Python/Apps/Android_Demo_App_V2.apk
output:
    Performing Streamed Install
    Success
```
> If it is blocked try:
> ```
> $ adb shell settings put global verifier_verify_adb_installs 0
> $ adb shell settings put global package_verifier_enable 0
> ```
> Install it and then, return them to 1
> ```
> $ adb shell settings put global verifier_verify_adb_installs 1
> $ adb shell settings put global package_verifier_enable 1
> ```

## Uninstall the app
1. Open the app to uninstall
2. Run `adb shell dumpsys window windows | grep imeLayeringTarget`
    > Run
    >
    > ```
    > $ adb shell dumpsys window windows | grep imeLayeringTarget
    >
    > output:
    >
    >    imeLayeringTarget in display# 0 Window{5794baa u0 com.code2lead.kwad/com.code2lead.kwad.MainActivity}
    > ```
3. Run
    ```
    $ adb uninstall com.code2lead.kwad
    output:
        Success
    ```

## Restart adb
```
$ adb kill-server
$ adb start-server
```

## Take screenshot
1. Find location to save screenshot `/sdcard`
    ```
    $ adb shell
        dm1q:/ $ ls
        output:
            acct                efs                prism
            apex                etc                proc
            audit_filter_table  init               product
            bin                 init.container.rc  sdcard
            bugreports          init.environ.rc    second_stage_resources
            cache               linkerconfig       sepolicy_version
            carrier             metadata           storage
            config              mnt                sys
            d                   odm                system
            data                odm_dlkm           system_dlkm
            data_mirror         oem                system_ext
            debug_ramdisk       omr                vendor
            dev                 optics             vendor_dlkm
            dpolicy_system      postinstall
        
        dm1q:/ $ cd sdcard

        dm1q:/sdcard $ ls
        output:
            Alarms      DCIM       Movies         Pictures    Ringtones
            Android     Documents  Music          Podcasts
            Audiobooks  Download   Notifications  Recordings
        
        dm1q:/ $ exit
    ```
2. Open the app in the device
3. Take the screenshot from the terminal
    ```
    adb shell screencap -p /sdcard/code2lead.png
    ```
4. Verify the saved image
    ```
    adb shell 
        dm1q:/ $ cd sdcard
        
        dm1q:/sdcard $ ls
        output:
            Alarms      DCIM       Movies         Pictures    Ringtones
            Android     Documents  Music          Podcasts    code2lead.png
            Audiobooks  Download   Notifications  Recordings
        
        dm1q:/ $ exit
    ```

## Pull files from device to pc
    ```
    adb pull /sdcard/code2lead.png ~/Documents/Courses/Appium-Python/material/device_pullted_images
    output:
        /sdcard/code2lead.png: 1 file pulled, ...ed. 11.3 MB/s (158590 bytes in 0.013s)
    ```

## Push files from pc to device
1. Run
    ```
    $  adb push ~/Documents/Courses/Appium-Python/Apps/Android_Demo_App_V2.apk /sdcard/
    output:
        /Users/j.escalante/Documents/Courses/A...d. 87.8 MB/s (2836897 bytes in 0.031s)
    ```
2. Verify file in device
    ```
    $ adb shell
        dm1q:/ $ cd /sdcard/  

        dm1q:/sdcard $ ls
        output:
            Alarms                   Audiobooks  Download  Notifications  Recordings
            Android                  DCIM        Movies    Pictures       Ringtones
            Android_Demo_App_V2.apk  Documents   Music     Podcasts       code2lead.png
        
        dm1q:/ $ exit
    ```


## Find Main Activity
```
adb shell pm list packages | grep telus         # List pkgs
adb shell pm dump com.telus.myaccount.dev | grep -A 1 MAIN      # List main activities
```

## Record android screen
1. Open the app to record in the device
2. Start recording
    ```
    $ adb shell screenrecord /sdcard/code2lead.mp4
    ```
3. Stop recording by pressing `ctrl + C`
4. Verify file `code2lead.mp4` exist in `sdcard` folder
    ```
    $ adb shell
        dm1q:/ $ cd /sdcard/   

        dm1q:/sdcard $ ls
            Alarms                   DCIM       Music          Recordings
            Android                  Documents  Notifications  Ringtones
            Android_Demo_App_V2.apk  Download   Pictures       code2lead.mp4
            Audiobooks               Movies     Podcasts       code2lead.png
        
        dm1q:/sdcard $ exit
    ```
5. Pull the file from device to pc
    ```
    $ adb pull /sdcard/code2lead.mp4 ~/Documents/Courses/Appium-Python/material/device_pullted_images
    output:
        /sdcard/code2lead.mp4: 1 file pulled, .... 40.2 MB/s (19730166 bytes in 0.468s)
    ```

## Launch app using adb
    ```
    $ adb shell am start -W -n com.code2lead.kwad/com.code2lead.kwad.MainActivity
    ourput:
        Starting: Intent { cmp=com.code2lead.kwad/.MainActivity }
        Status: ok
        LaunchState: COLD
        Activity: com.code2lead.kwad/.MainActivity
        TotalTime: 304
        WaitTime: 308
        Complete
    ```

## Tap using XY coordinates
1. Activate
    > Settings → Developer options → Input Section → Pointer location
   Or you can use Android Inspector to look for Coordinates
2. Open the app
    ```
    $ adb shell am start -W -n com.code2lead.kwad/com.code2lead.kwad.MainActivity
    ```
3. Click on ScrollView Button using coordinates
    ```
    $ adb shell input tap 515 1090
    ```

## Enter text using adb command
1. Open the app
    ```
    $ adb shell am start -W -n com.code2lead.kwad/com.code2lead.kwad.MainActivity
    ```
2. Click on ScrollView Button using coordinates
    ```
    $ adb shell input tap 515 1090
    ```
3. Enter some text
    ```
    $ adb shell input text "code2lead"
    ```


## adb keyevents
[More](https://stackoverflow.com/questions/7789826/adb-shell-input-events)
1. Open the app and go to `Enter Some Value`
    ```
    $ adb shell am start -W -n com.code2lead.kwad/com.code2lead.kwad.MainActivity
    $ adb shell input tap 515 1090   # Enter Some Value btn
    $ adb shell input text "code2lead"
    ```
2. Go back (code: 4)
    ```
    $ adb shell input keyevent 4
    ```

## Swipe using adb
1. Open the app and click on the `Tab Activity` btn
    ```
    $ adb shell am start -W -n com.code2lead.kwad/com.code2lead.kwad.MainActivity
    $ adb shell input tap 507 1639   # Tab Activity btn
    ```
2. Swipe to left
    ```
    $ adb shell input swipe 1070 1210 10 1210
    ```
3. Swipe to right
    ```
    adb shell input swipe 10 1210 1070 1210
    ```

## Reboot the device
    ```
    $ adb reboot
    ```

## Wireless device connection
[Source](https://stackoverflow.com/questions/33462720/adb-unable-to-connect-to-192-168-1-105555)
1. Verify both (phone and computer) are connected to same wireless
2. Unplug USB
3. Restart Android device
4. Shutdown Android Studio or any other IDE using ADB
5. `adb kill-server`
6. Plug back in USB after restart
7. `adb devices` This automatically starts the server. You sould see the device plugged in via USB
8. `adb shell ip addr show wlan0` to get your devices IP address
    > Also: settings → About phone → status → ip adress
9. `adb tcpip 5555` Set the port to 5555 that you want to connect through
10. `adb connect 192.168.1.33:5555` Replace IP address with one from step 7.
11. Disconnect the USB
12. `adb devices` to confirm it is available


## Collect logs using adb
- To get the logcat log
    ```
    $ adb logcat
    ```
- To clean the log
    ```
    $ adb logcat --clear 
    ```
- To filter the log output
    ```
    $ adb logcat -t '2024-12-27 0:30:10.55'
    ```
- To save it in a file
    ```
    $ adb logcat >> ~/Documents/Courses/Appium-Python/material/device_pullted_images/code2lead.log
    ```
    > Look for `runtime`

# Android Studio
1. Create `New project`
2. Select `Empty Activity`
3. Fill the form
    - Name: AppiumTest
    - Pkg name: com.example.appiumtest
    - Save location: /Users/j.escalante/Documents/Courses/Appium-Python/AppiumConceptsAndroid
    - Minimum SDK

# To solve issue
1. ADB server didn't ACK >> Disconnect VPN
