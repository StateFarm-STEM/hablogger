from machine import Pin, SPI, I2C, UART
from drivers import sdcard
from drivers import gtu7 as gpsdriver
from drivers import bmp180 as bmp180driver
from ssd1306 import SSD1306_I2C

import os


class Logger():
    def __init__(self) :
        self.oled = self.__init_oled()
        
    def disp(self, text, pos):
        self.oled.text(text, pos[0], pos[1])
        self.oled.show()
        
    def __init_oled(self):
        # https://www.tomshardware.com/how-to/oled-display-raspberry-pi-pico
        i2c = I2C(1,
                sda=Pin(14),
                scl=Pin(15),
                freq = 400000)
        oled = SSD1306_I2C(128, 64, i2c) # width is 128, height is 64
        
        return oled


def logger(text):
    print("text")


def init_bmp180(test=False):
    bus =  I2C(0,
               scl=Pin(17),
               sda=Pin(16),
               freq=100000)

    # Initialize BMP180 with previously defined I2C config
    bmp180 = bmp180driver.BMP180(bus)
    
    bmp180.oversample_sett = 2 # Accuracy, as defined in driver docs: https://github.com/micropython-IMU/micropython-bmp180
    bmp180.baseline = 101325   # Baseline pressure, as defined in driver docs: https://github.com/micropython-IMU/micropython-bmp180

    if test:
        try:
            assert isinstance(bmp180.temperature, float)
        except AssertionError:
            log.disp("BMP180_TEMP: ERR", [0,0])
        else:
            log.disp("BMP180_TEMP: OK", [0,0])

        try:
            assert isinstance(bmp180.pressure, float)
        except AssertionError:
            log.disp("BMP180_PRES: ERR", [0,10])
        else:
            log.disp("BMP180_PRES: OK", [0,10])

        try:
            assert isinstance(bmp180.altitude, float)
        except AssertionError:
            log.disp("BMP180_ALTI: ERR", [0,20])
        else:
            log.disp("BMP180_ALTI: OK", [0,20])
            
        print("read prompt timer")

    return bmp180


def init_gtu7():
    uart = UART(1,
                baudrate=9600,
                timeout=3600,
                tx=Pin(4),
                rx=Pin(5))

    gtu7 = gpsdriver.GTU7(uart)

    return gtu7


def init_sdcard(folder, mount=True):
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
    
    if mount:
        os.mount(sd,folder)
    else:
        os.umount(folder)


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
    print("Deleting files from '%s'..." % folder)
    for file in os.listdir(folder)[1:]:
        os.remove(folder + '/' + file)
            
            
if __name__ == "__main__":          
    log = Logger()  # create Logger object which allows logging to OLED module
    #log.disp('Hello, World 0!', [0, 0])
    
    led = Pin(25, Pin.OUT)  # Assign onboard LED to variable
    led.toggle()
    
    sd_dir = '/sd'          # Directory created on SD card at root '/'. Expected format is '/<string>'. Example: '/sd'
    init_sdcard(sd_dir)     # Initialize the SD Card
    
    bmp180 = init_bmp180(True)  # Initialize the BMP_180 (Temp/Pressure module)
    gtu7 = init_gtu7()      # Initialize the GT-U7 (GPS module)

    delete_files_from_sdcard_folder('/sd') # This helper function cleans up the SD card. Uncomment this to delete SD card data.

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
    
    for x in range(1):
        temp = bmp180.temperature  # Capture temperature, assign to `temp` variable
        p = bmp180.pressure        # Capture pressure, assign to `p` variable
        altitude = bmp180.altitude # Capture altitude, assign to `altitude` variable
        
        gpgga = gtu7.gpgga() # Capture NMEA GPGGA GPS data (http://aprs.gids.nl/nmea/#gga)
        gprmc = gtu7.gprmc() # Capture NMEA GPRMC GPS data (http://aprs.gids.nl/nmea/#rmc)
        
        data = [gprmc[0], gprmc[1], gprmc[2], gprmc[3], gprmc[4], gpgga[3], temp, p, altitude]
        
        write_csv_to_sdcard(sd_dir, "data.csv", data)
    
    # Read all the rows from the CSV and print them to the console.
    for row in read_csv_from_sdcard(sd_dir, "data.csv"):
        print(row)

    led.toggle()
