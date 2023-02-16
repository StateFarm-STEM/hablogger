from machine import Pin, SPI, I2C, UART
from drivers import sdcard
from drivers import gtu7 as gpsdriver
from drivers import bmp180 as bmp180driver
from ssd1306 import SSD1306_I2C

import os
import time
import _thread
    
    
def init_oled():
    # https://www.tomshardware.com/how-to/oled-display-raspberry-pi-pico
    i2c = I2C(0,
            sda=Pin(16),
            scl=Pin(17),
            freq = 400000)
    
    oled = SSD1306_I2C(128, 64, i2c) # width is 128, height is 64
    
    return oled


def init_bmp180(test=True):
    bus =  I2C(0,
               sda=Pin(16),
               scl=Pin(17),
               freq=100000)

    # Initialize BMP180 with previously defined I2C config
    bmp180 = bmp180driver.BMP180(bus)
    
    bmp180.oversample_sett = 2 # Accuracy, as defined in driver docs: https://github.com/micropython-IMU/micropython-bmp180
    bmp180.baseline = 101325   # Baseline pressure, as defined in driver docs: https://github.com/micropython-IMU/micropython-bmp180

    if test:
        try:
            assert isinstance(bmp180.temperature, float)
        except AssertionError:
            oled.text("BMP180_TEMP: ERR", 0, 0)
        else:
            oled.text("BMP180_TEMP: OK", 0, 0)

        try:
            assert isinstance(bmp180.pressure, float)
        except AssertionError:
            oled.text("BMP180_PRES: ERR", 0,10)
        else:
            oled.text("BMP180_PRES: OK", 0, 10)

        try:
            assert isinstance(bmp180.altitude, float)
        except AssertionError:
            oled.text("BMP180_ALTI: ERR", 0, 20)
        else:
            oled.text("BMP180_ALTI: OK", 0, 20)
            
        oled.show()

    return bmp180


def init_gtu7(test=True):
    uart = UART(1,
                baudrate=9600,
                timeout=3600,
                tx=Pin(4),
                rx=Pin(5))

    gtu7 = gpsdriver.GTU7(uart)
    
    if test:
        try:
            assert len(gtu7.gpgga()) == 4
        except AssertionError:
            oled.text("GTU7_GPGGA : ERR", 0, 30)
        else:
            oled.text("GTU7_GPGGA : OK", 0, 30)

        try:
            assert len(gtu7.gprmc()) == 5
        except AssertionError:
            oled.text("GTU7_GPRMC : ERR", 0,40)
        else:
            oled.text("GTU7_GPRMC : OK", 0, 40)
            
        oled.show()

    return gtu7


def init_sdcard(folder, test=True):
    spi = machine.SPI(1,
                      baudrate=1000000,     # 1 MHz
                      polarity=0,
                      phase=0,
                      bits=8,
                      firstbit=SPI.MSB,
                      sck=machine.Pin(10),  # Pico GPIO Pin 10
                      mosi=machine.Pin(11), # Pico GPIO Pin 11
                      miso=machine.Pin(12)) # Pico GPIO Pin 12
    sd = sdcard.SDCard(spi,Pin(13))
    
    os.mount(sd,folder)
    
    if test:
        try:
            assert folder[1:] in os.listdir()
        except AssertionError:
            oled.text("SD_CARD    : ERR", 0, 50)
        else:
            oled.text("SD_CARD    : OK", 0, 50)
            
        oled.show()


def write_csv_to_sdcard(folder, file_name, dataset, header=None):
    with open(folder + '/' + file_name,'a+') as csv_out:
        if header:
            dataset = header
            
        for data in dataset:
            if data == dataset[-1]:
                # If last element in the dataset, don't add a comma.
                csv_out.write('"'+str(data)+'"')
            else:
                csv_out.write('"'+str(data)+'",')
        csv_out.write('\n')


def read_csv_from_sdcard(folder, file_name):
    csv_data = []
    with open(folder + '/' + file_name,'r') as csv_in:
        for line in csv_in:
            line=line.rstrip('\n')
            line=line.rstrip('\r')
            csv_data.append(line.split(','))

    return csv_data


def delete_files_from_sdcard_folder(folder):
    for file in os.listdir(folder):
        try:
            os.remove(folder + '/' + file)
        except Exception as e:
            pass
            
            
if __name__ == "__main__":   
    led = Pin(25, Pin.OUT)  # Assign onboard LED to variable
    led.toggle()            # Toggle on the onboard LED
    
    oled = init_oled()      # Initialize the OLED display module
    
    try:
        sd_dir = '/sd'          # Directory created on SD card at root '/'. Expected format is '/<string>'. Example: '/sd'
        init_sdcard(sd_dir)     # Initialize the SD Card
        
        bmp180 = init_bmp180()  # Initialize the BMP_180 (Temp/Pressure module)
        gtu7 = init_gtu7()      # Initialize the GT-U7 (GPS module)

        delete_files_from_sdcard_folder('/sd') # Uncomment this to delete a folder and its contents.
        
        # Start a new thread and power off the OLED after a certain amount of time (in seconds)
        oled_off = lambda: (time.sleep(30), oled.poweroff())
        _thread.start_new_thread(oled_off, ())

        csv_header = [
            "date",
            "time",
            "latitude",
            "longitude",
            "velocity",
            "numSatellites",
            "temperature",
            "pressure",
            "altitude",
            ]
        write_csv_to_sdcard(sd_dir, "data.csv", None, csv_header) # Initialize CSV header
        
        for x in range(10):
            temp = bmp180.temperature  # Capture temperature, assign to `temp` variable
            p = bmp180.pressure        # Capture pressure, assign to `p` variable
            altitude = bmp180.altitude # Capture altitude, assign to `altitude` variable
            
            gpgga = gtu7.gpgga() # Capture NMEA GPGGA GPS data (http://aprs.gids.nl/nmea/#gga)
            gprmc = gtu7.gprmc() # Capture NMEA GPRMC GPS data (http://aprs.gids.nl/nmea/#rmc)
            
            data = [gprmc[0], gprmc[1], gprmc[2], gprmc[3], gprmc[4], gpgga[3], temp, p, altitude]
            
            write_csv_to_sdcard(sd_dir, "data.csv", data)
            
    except Exception as e:
        print(e)
        oled.fill(False)
        oled.text(str(e), 0, 0)
        oled.show()
        
    # Read all the rows from the CSV and print them to the console.
    #for row in read_csv_from_sdcard(sd_dir, "data.csv"):
    #    print(row)
    
    led.toggle() # Toggle off the onboard LED
