"""Perform the following actions:
- Run Demo App on Android device.
"""
import time
from devices.AvailableDevices import GetDriver


# Step 1: Create "Desired Capabilities"
# Step 2: Web Driver Object 
driver = GetDriver(device='IOS18')

# Step 3: Close the driver object
time.sleep(5)
driver.quit()
