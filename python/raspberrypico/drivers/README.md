# Drivers
Drivers are useful extension of modules attached to the Raspberry Pi Pico. In all cases they simplify writing Python code to handle information read, or written to a module without the complexity of managing the complex coded required to do so.

Each lesson with an attached module is paired with a driver (GPS, SD Card, Atmospheric).

## BPM-180 Driver for Raspberry Pi Pico

This driver was originally found within the [micropython-IMU](https://github.com/micropython-IMU/micropython-bmp180) project, but requires some modification to work with our project. Commenting out `self._bmp_i2c.start()` solves an initialization error, otherwise leaving the driver completely functional for our use case.

## GT-U Driver for Raspberry Pi Pico

This driver is perhaps less a driver and more a simplification of handling the streaming inputs from the GPS module itself. It was written specifically for the HABlogger project.

### GPS data returned from GT-U7 module

All GPS sentence data can be found at the [NMEA sentence information](http://aprs.gids.nl/nmea/) website.

|$GPXXX  | Description |
| ------ | ----------- |
| $GPGGA | Global Positioning System Fix Data. 3D location and accuracy data. |
| $GPGSA | GPS DOP and active satellites |
| $GPGSV | Detailed information of the GPS satellite |
| $GPGLL | Geographic Latitude and Longitude |
| $GPRMC | Position, velocity and time |
| $GPVTG | Dual ground/water speed |

## SD Card Driver for Raspberry Pi Pico

MicroPython offers a functional driver for a standard SD card module. The steps below can be used to download the latest version of the driver if needed.

1. Download the latest version of the `sdcard.py` driver from [MicroPython](https://github.com/micropython/micropython)
    1. Navigate to the [MicroPython releases](https://github.com/micropython/micropython/releases/) page.
    1. Click on the latest release tag (for example, v1.19)
    1. Click the `/drivers` folder
    1. Click the `/sdcard` folder
    1. Click the _Raw_ button in the top right of the file
    1. Download, or otherwise save the file to your computer as `sdcard.py`
    1. As an example, here is a direct link to v1.19 of the `sdcard.py` driver: https://raw.githubusercontent.com/micropython/micropython/v1.19/drivers/sdcard/sdcard.py
