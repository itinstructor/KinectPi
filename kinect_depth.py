"""
File: kinect_depth.py
Description: Get and display a depth map from a Kinect XBox 360
"""

import freenect
import cv2
import numpy as np


# A function to get the depth map from the Kinect
def get_depth():
    array, _ = freenect.sync_get_depth()
    # The freenect library gives 11-bit depth data.
    # We need to convert it to 8-bit (0-255) for OpenCV to display.
    array = array.astype(np.uint8)
    return array


# Main loop
while True:
    # 1. Get a depth frame
    depth_map = get_depth()

    # 2. Display the frame
    # 'Depth Map' is the name of the window
    cv2.imshow("Depth Map", depth_map)

    # 3. Check for a key press
    # Wait 10 milliseconds. If 'q' is pressed, break the loop.
    key = cv2.waitKey(10)
    if key == ord("q"):
        break

# Clean up
cv2.destroyAllWindows()
freenect.sync_stop()
