# KinectPi

Kinect Xbox 360 and Raspberry pi

## Manual Setup

1. Install the libfreenect-dev package

```Python
sudo apt update
sudo apt upgrade -y
sudo apt install libfreenect-dev
```

2. Create a folder and a Python virtual environment

```bash
mkdir KinectPi

# Create a Python virtual environment
python -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install required packages
pip install freenect numpy opencv-python
```

3. Plug in the power to the Kinect
4. Connect USB to Pi
5. Run the programs


```Python
# Test the Kinect
python kinect_test.py

# Depth display depth map
python kinect_depth.py
```

### License

[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

Copyright (c) 2025 William A Loring