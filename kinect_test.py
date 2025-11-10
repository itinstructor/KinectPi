import freenect

print("Attempting to connect to Kinect...")

try:
    # Try to get one depth frame
    array, _ = freenect.sync_get_depth()

    if array is None:
        print("\nError: sync_get_depth() returned None.")
        print("This almost always means another program is using the Kinect.")
        print("Please reboot and try running this script *only*.")
    else:
        print(f"\nSUCCESS! Got one depth frame.")
        print(f"Data shape: {array.shape}, Data type: {array.dtype}")

except Exception as e:
    print(f"\nA fatal error occurred: {e}")
finally:
    # This is important to shut down the freenect context
    freenect.sync_stop()
    print("Freenect context stopped.")
