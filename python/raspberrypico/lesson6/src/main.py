from machine import Pin, SPI, I2C, UART
from drivers import sdcard
from drivers import gtu7 as gpsdriver
from drivers import bmp180 as bmp180driver

import os


def initBmp180() :
    bus =  I2C(0,
               scl=Pin(17),
               sda=Pin(16),
               freq=100000)


    # Initialize BMP180 with previously defined I2C config
    bmp180 = bmp180driver.BMP180(bus)
    
    bmp180.oversample_sett = 2 # Accuracy, as defined in driver docs: https://github.com/micropython-IMU/micropython-bmp180
    bmp180.baseline = 101325   # Baseline pressure, as defined in driver docs: https://github.com/micropython-IMU/micropython-bmp180

    return bmp180


def initGtu7() :
    uart = UART(1,
                baudrate=9600,
                timeout=3600,
                tx=Pin(4),
                rx=Pin(5))

    gtu7 = gpsdriver.GTU7(uart)

    return gtu7


def initSDCard(sd_dir) :
    spi = machine.SPI(1,
                      baudrate=1000000,     # 1 MHz
                      polarity=0,
                      phase=0,
                      bits=8,
                      firstbit=SPI.MSB,
                      sck=machine.Pin(10),  # Pico GPIO Pin 10
                      mosi=machine.Pin(11), # Pico GPIO Pin 11
                      miso=machine.Pin(12)) # Pico GPIO Pin 12
    sd=sdcard.SDCard(spi,Pin(13))
     
    os.mount(sd,sd_dir)


def writeCsvToSDCard(sd_dir, file_name, dataset, header=None) :
    with open(sd_dir + '/' + file_name,'a+') as csv_out :
        if header :
            dataset = header
            
        for data in dataset :
            if data == dataset[-1] :
                # If last element in the dataset, don't add a comma.
                csv_out.write('"'+str(data)+'"')
            else :
                csv_out.write('"'+str(data)+'",')
        csv_out.write('\n')


def readCsvFromSDCard(sd_dir, file_name) :
    csv_data = []
    with open(sd_dir + '/' + file_name,'r') as csv_in :
        for line in csv_in:
            line=line.rstrip('\n')
            line=line.rstrip('\r')
            csv_data.append(line.split(','))

    return csv_data


def cleanupDirSDCard(rmdir) :
    print("Deleting files from '%s'..." % rmdir)
    for file in os.listdir(rmdir)[1:] :
        os.remove(rmdir + '/' + file)


if __name__ == "__main__" :   
    led = Pin(25, Pin.OUT)  # Assign on board LED to variable
    led.toggle()
    
    sd_dir = '/sd'          # Directory created on SD card at root '/'. Expected format is '/<string>'. Example: '/sd'
    initSDCard(sd_dir)
    
    bmp180 = initBmp180()   # Initialize the BMP_180 (Temp/Pressure module)
    gtu7 = initGtu7()       # Initialize the GT-U7 (GPS module)
    
    cleanupDirSDCard(sd_dir) # This helper function cleans up the SD card. Uncomment this to delete SD card data.

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
    writeCsvToSDCard(sd_dir, "data.csv", None, csv_header) # Initialize CSV header
    
    for x in range(10) :
        temp = bmp180.temperature  # Capture temperature, assign to `temp` variable
        p = bmp180.pressure        # Capture pressure, assign to `p` variable
        altitude = bmp180.altitude # Capture altitude, assign to `altitude` variable
        
        gpgga = gtu7.gpgga() # Capture NMEA GPGGA GPS data (http://aprs.gids.nl/nmea/#gga)
        gprmc = gtu7.gprmc() # Capture NMEA GPRMC GPS data (http://aprs.gids.nl/nmea/#rmc)
        
        data = [gprmc[0], gprmc[1], gprmc[2], gprmc[3], gprmc[4], gpgga[3], temp, p, altitude]
        
        writeCsvToSDCard(sd_dir, "data.csv", data)
    
    # Read all the rows from the CSV and print them to the console.
    for row in readCsvFromSDCard(sd_dir, "data.csv") :
        print(row)

    led.toggle()
