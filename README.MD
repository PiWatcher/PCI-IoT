# PCI-Prototype-RaspberryPi


## Downloading the OS Image to Micro SD
- Here is a link to the website where you can download the latest image (Note: The latet image may have differences in how to set the Pi up)
- https://www.raspberrypi.org/downloads/raspberry-pi-os/ (We reccomend downloading the image without the recommended software)
- Our version of the image -> Version:  August 2020

## Installing the OS Image to Micro SD
- Once you have the image you can then download software to to write the image to an sd card
- Here is the software we used to so just that http://sourceforge.net/projects/win32diskimager/
- Run the Win32DiskImager utility from your desktop or menu.
- Select the image file you extracted earlier.
- In the device box, select the drive letter of the SD card. Be careful to select the correct drive: if you choose the wrong drive you could destroy the data on your computer's hard disk! If you are using an SD card slot in your computer, and can't see the drive in the Win32DiskImager window, try using an external SD adapter.
- Click 'Write' and wait for the write to complete.
- Exit the imager and eject the SD card.

## Booting up the Raspberry Pi
- Inset the sd card into the Pi
- Boot up the Pi and plug it into a proper display
- Follow the set-up menu provided
- You have sucessfully installed the Raspberry Pi OS



## Cloning The Repo Onto The Pi
- Open up a terminal window on the Raspoberry Pi
- Run the following command <br>
HTTPS: 
```console
git clone https://github.com/PiWatcher/PCI-Prototype-IoT.git
``` 
<br>
SSH: 
```console
git@github.com:PiWatcher/PCI-Prototype-IoT.git
```

## Installing dependancies
- After repo has been cloned cd into it
- Run the following command <br>
```console
. setup.sh
``` 
<br>
Now follow any prompts on the shell
- This will install the correct version of Python along with any dependancies needed into a virtual enviornment that will be placed into the Pi's Home Directory

## Starting/Deactivating the Virtual Enviornment
- To start the virtual enviornment:<br>
```console
source ~/env/PiEnv/bin/activate
```
- To deactivate the virtual enviornment:<br>
```console
deactivate
```

## Running the Application
- To run the application ensure you are in the cloned folder and the virtual enviornment is running then execute the command below <br>
```console
python scheduler.py
```

Make sure to manually add the checkpoints folder to the root directory of this repo from the capstone drive

https://drive.google.com/file/d/123C8nYOtgUemRZKsUipiOc0CxIWqyk5V/view?usp=sharing

