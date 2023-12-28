from machine import Pin, SPI, I2C, UART
from drivers import sdcard
from drivers import gtu7 as gpsdriver
from drivers import bmp180 as bmp180driver

import os

def init_bmp180():
    """Initialize the BMP-180 Barometric Pressure/Temperature/Altitude Sensor"""
    bus =  I2C(0,
               sda=Pin(16),
               scl=Pin(17),
               freq=100000)

    # Initialize BMP180 with previously defined I2C config
    bmp180 = bmp180driver.BMP180(bus)
    
    bmp180.oversample_sett = 2 # Accuracy, as defined in driver docs: https://github.com/micropython-IMU/micropython-bmp180
    bmp180.baseline = 101325   # Baseline pressure, as defined in driver docs: https://github.com/micropython-IMU/micropython-bmp180

    return bmp180


def init_gtu7():
    """Initialize the GTU-7 GPS module"""
    uart = UART(1,
                baudrate=9600,
                timeout=3600,
                tx=Pin(4),
                rx=Pin(5))

    gtu7 = gpsdriver.GTU7(uart)
    #gtu7.setGPS_DynamicMode6() #uncomment for high altitude mode. Only works with ublox branded GPS chips.

    return gtu7


def init_sdcard(folder):
    """Initialize SD Card module and mount SD card"""
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
    
    # Mount SD card using sd card library and folder name
    #os.mount(sd,folder)
    # Some SD cards require another mount attempt to function
    try:
        print("Attempting mount...")
        os.mount(sd,folder)
    except:
        print("Second mount attempt...")
        os.mount(sd,folder)


def write_csv_to_sdcard(folder, file_name, dataset, header=None):
    """Write CSV data to SD Card"""
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
    """Read CSV file from SD Card"""
    csv_data = []
    with open(folder + '/' + file_name,'r') as csv_in:
        for line in csv_in:
            line=line.rstrip('\n')
            line=line.rstrip('\r')
            csv_data.append(line.split(','))

    return csv_data


def delete_files_from_sdcard_folder(folder):
    """Delete all files from SD Card folder"""
    for file in os.listdir(folder):
        try:
            os.remove(folder + '/' + file)
        except Exception as e:
            pass
            
            
if __name__ == "__main__":
    """Start of the main program. All functions are called form here."""
    
    sd_dir = '/sd'          # Directory created on SD card at root '/'. Expected format is '/<string>'. Example: '/sd'
    init_sdcard(sd_dir)     # Initialize the SD Card
    
    bmp180 = init_bmp180()  # Initialize the BMP_180 (Temp/Pressure module)
    gtu7 = init_gtu7()      # Initialize the GT-U7 (GPS module)

    delete_files_from_sdcard_folder('/sd') # Uncomment this to delete a folder and its contents.
                                           # This can be useful when you want to clean up the CSV file.

    # We set the CSV column headers here. Be sure these headers line up with the data you are
    # reading in and writing to the CSV.
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
    
    print("Reading data from sensors and writing CSV to SD card...")
    for x in range(30):
        temp = bmp180.temperature  # Capture temperature, assign to `temp` variable
        p = bmp180.pressure        # Capture pressure, assign to `p` variable
        altitude = bmp180.altitude # Capture altitude, assign to `altitude` variable
        
        gpgga = gtu7.gpgga() # Capture NMEA GPGGA GPS data (http://aprs.gids.nl/nmea/#gga)
        gprmc = gtu7.gprmc() # Capture NMEA GPRMC GPS data (http://aprs.gids.nl/nmea/#rmc)
        
        # These are the data elements we want to line up with our CSV column headers
        data = [gprmc[0], gprmc[1], gprmc[2], gprmc[3], gprmc[4], gpgga[3], temp, p, altitude]
        
        print(data)
        
        write_csv_to_sdcard(sd_dir, "data.csv", data)
    print("Done.\n\n")
        
    # Read all the rows from the CSV and print them to the console.
    print("Reading and printing data from SD card...")
    for row in read_csv_from_sdcard(sd_dir, "data.csv") :
        print(row)
    print("Done.\n\n")
