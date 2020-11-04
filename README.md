# PCI-Prototype-RaspberryPi


## Downloading the OS Image to Micro SD
- To use our version of the image you can download it from our folder titled Raspberry Pi OS
- Here is a link to the website where you can download the latest image (Note: The latet image may have differences in how to set the Pi up)
- https://www.raspberrypi.org/downloads/raspberry-pi-os/ (We reccomend downloading the image without the recommended software)

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



## Installing OpenCV
- Run the command ```shell sudo pip3 install opencv-contrib-python``` in the terminal 
