"""Perform the following actions:
- Run Demo App on Android device.
- Review some available ios methods
"""
import time
from devices.AvailableDevices import GetDriver


# Step 1: Create "Desired Capabilities"
# Step 2: Web Driver Object 
driver = GetDriver(device='IOS18')

# Step 3: Actions to execute
print(f"""
Is device locked?  : {driver.is_locked()}
Current orientation: {driver.orientation}
Current context    : {driver.current_context}
""")

# Step 4: Close the driver object
time.sleep(5)
driver.quit()
