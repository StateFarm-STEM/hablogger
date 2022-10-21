# hablogger
 High Altitude Balloon Data Logging 

* [Raspberry Pi Pico Pinout](https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf)
* [Raspberry Pi Pico SDK](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf)
* [MicroPython releases for Pico](https://micropython.org/download/rp2-pico/)
* [MicroPython libraries](https://docs.micropython.org/en/latest/library/index.html)
 

 ## HW-150 SD Card Reader
 * Control Interface: A total of six pins (GND, VCC, MISO, MOSI, SCK, CS), GND to ground, VCC is the power supply, MISO, MOSI, SCK for SPI bus, CS is the chip select signal pin;


 ## Steps:
 1. Format SD card as `FAT32` with a small block size (optimized for writes for this project)
 1. Download the latest version of `sdcard.py` from MicroPython/drivers/sdcard: https://github.com/micropython/micropython/tree/v1.19/drivers/sdcard
 1. Create a new directory in Thonny on the Raspberry Pi Pic called `drivers`
 1. Using Thonny, open the `sdcard.py` file. Then save the `sdcard.py` file to the Raspberry Pi Pico using Save As. Save it to the `/drivers` directory and call it `sdcard.py`.
 1. Create a new file in Thonny called `__init__.py`. Save this file to the same location as above (the file will be empty).
