# KinectPi

Kinect Xbox 360 and Raspberry Pi Projects

Becuase of the processing needed, we are using a Raspberry Pi 5.

## Manual Setup

1. Switch the raspberry pi to X11 display manager

```bash
Go to a terminal prompt
sudo raspi-config
1. Advanced Options
A7 Wayland
Select: W1 X11
Tab to Ok
Press Enter
You will be asked to reboot.
```

2. Install the libfreenect-dev package

```Python
sudo apt update
sudo apt upgrade -y
sudo apt install libfreenect-dev
```

3. Pull the KinectPi repository

```bash
git clone https://github.com/itinstructor/KinectPi.git

cd KinectPi

# Create a Python virtual environment
python -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install required packages
pip install freenect numpy opencv-python
```

4. Plug in the power to the Kinect

5. Connect Kinect to a USB port on the Pi

6. Test the Pi's connection to the Kinect

```Python
# Test the Kinect
python kinect_test.py
CTRL-C to exit

# Depth display depth map
python kinect_depth.py
CTRL-C to exit
```

7. Update the code

```bash
git pull https://github.com/itinstructor/KinectPi.git
```

## Automated Setup

Coming soon . . .

### License

[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

Copyright (c) 2025 William A Loring