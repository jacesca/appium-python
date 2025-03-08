"""
Multiple launch example.
Run 
`python -m AppiumConcepts.LaunchMultipleApps.LaunchMultiApps`

This scripst ope the demo app, then open the youtube app, and then return to the demp app.
"""
import time
from appium.webdriver.common.appiumby import AppiumBy
from devices.AvailableDevices import GetDriver


# Step 1: Create "Desired Capabilities"
# Step 2: Web Driver Object 
driver = GetDriver(device='GalaxyS23')
time.sleep(2)

# Step 3: Action to execute - Open YouTube
driver.execute_script(
    'mobile: startActivity',
    {
        # 'intent': 'com.android.vending/com.android.vending.AssetBrowserActivity',   # PlayStore
        'component': r'com.google.android.youtube/com.google.android.youtube.app.honeycomb.Shell\$HomeActivity',   # YouTube
    }
)
time.sleep(5)

# Return to the Demo app
driver.execute_script(
    'mobile: startActivity',
    {
        'component': 'com.code2lead.kwad/com.code2lead.kwad.MainActivity',   # Demo App
    }
)
time.sleep(2)


# Close Apps
driver.terminate_app('com.google.android.youtube')
driver.terminate_app('com.code2lead.kwad')

# Step 4: Close the driver object
time.sleep(5)
driver.quit()
