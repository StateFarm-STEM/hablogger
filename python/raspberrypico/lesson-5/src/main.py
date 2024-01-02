from machine import Pin, SPI
from drivers import sdcard
from time import gmtime

import os

# ---------------------------
# This project uses the `sdcard.py` MicroPython driver to interface with a
# HW-125 SDCard peripheral attached to a Raspberry Pi Pico.
# 
# Example information is written to a CSV file, then read and printed to the console.
# An optional function can be used to delete the files in the SD card directory.

def write_csv_to_sdcard(folder, file_name, dataset, header=None):
    """Write CSV data to SD Card"""

    # Open the file if it already exists. Otherwise create a new one.
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
    # Open the CSV file in read mode. Store each CSV line in a list called csv_data.
    with open(folder + '/' + file_name,'r') as csv_in:
        for line in csv_in:
            line=line.rstrip('\n')
            line=line.rstrip('\r')
            csv_data.append(line.split(','))

    return csv_data


if __name__ == "__main__":
    # Main entrypoint. Primary code functions start here.
    
    sd_dir = '/sd' # Directory created on SD card at root '/'. Expected format is '/<string>'. Example: '/sd'

    # Intialize SPI peripheral
    spi = machine.SPI(1,
                      baudrate=1000000,     # 1 MHz
                      polarity=0,
                      phase=0,
                      bits=8,
                      firstbit=SPI.MSB,
                      sck=machine.Pin(10),  # Pico GPIO Pin 10
                      mosi=machine.Pin(11), # Pico GPIO Pin 11
                      miso=machine.Pin(12)) # Pico GPIO Pin 12

    # Initialize the SD card to Pico GPIO Pin 13 on chip select (CS) pin
    sd = sdcard.SDCard(spi,Pin(13))
     
    # Mount the SD card at specified directory
    # Some SD cards require another mount attempt to function, so we use a Try Except to handle that.
    try:
        print("Attempting mount...")
        os.mount(sd,sd_dir)
    except:
        print("Second mount attempt...")
        os.mount(sd,sd_dir)
    
    print("Writing example data to SD card...")
    for x in range(6):
        # Example: temp, humidity, pressure, lat, long, alt, time
        dataset = [98.6, 84.5, 29.74, 40.4492267, -89.0431831, 244, str(gmtime())]
        write_csv_to_sdcard(sd_dir, "data.csv", dataset)
    print("Done.\n\n")
    
    # Read all the rows from the CSV and print them to the console.
    print("Reading and printing data from SD card...")
    for row in read_csv_from_sdcard(sd_dir, "data.csv") :
        print(row)
    print("Done.\n\n")
