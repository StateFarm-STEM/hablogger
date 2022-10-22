from machine import Pin, SPI, Timer
from drivers import sdcard
from time import sleep, gmtime

import os

# ---------------------------
# This project uses the `sdcard.py` MicroPython driver to interface with a
# HW-125 SDCard peripheral attached to a Raspberry Pi Pico.
# 
# Dummy information is written to a CSV file, then read and printed to the console.
# An optional function can be used to delete the files in the SD card directory.


def blinkLed(timer_one) :
    # Toggle LED functionality
    
    led.toggle()


def writeCsv(sd_dir, file_name, dataset) :
    # Write dataset to CSV using list dataset passed in.
    
    # Open a new file if it doesn't exist, otherwise append an existing file.
    print("Writing data to '%s/%s'..." % (sd_dir, file_name))
    with open(sd_dir + '/' + file_name,'a+') as csv_out :
        for data in dataset :
            if data == dataset[-1] :
                # If last element in the dataset, don't add a comma.
                csv_out.write('"'+str(data)+'"')
            else :
                csv_out.write('"'+str(data)+'",')
        csv_out.write('\n')
    print("Done.")


def readCsv(sd_dir, file_name) :
    # Returns a list of CSV rows.
    
    csv_data = []
    # Open the CSV file in read mode. Store each CSV line in a list called csv_data.
    print("Reading data from '%s/%s'..." % (sd_dir, file_name))
    with open(sd_dir + '/' + file_name,'r') as csv_in :
        for line in csv_in:
            line=line.rstrip('\n')
            line=line.rstrip('\r')
            csv_data.append(line.split(','))
    print("Done")

    return csv_data


def cleanupDir(rmdir) :
    # Deletes all the files in a directory passed in. Does not delete sub-directories.

    print("Deleting files from '%s'..." % rmdir)
    for file in os.listdir(rmdir)[1:] :
        os.remove(rmdir + '/' + file)
    print("Done.")


if __name__ == "__main__" :
    # Main entrypoint. Primary code functions start here.
    
    led = Pin(25, Pin.OUT)  # Assign on board LED to variable
    sd_dir = '/sd'          # Directory created on SD card at root '/'. Expected format is '/<string>'. Example: '/sd'
        
    # Initialize Timer() and blink the onboard LED until control interrupt (Stop/Restart backend)
    machine.Timer().init(freq=1, mode=Timer.PERIODIC, callback=blinkLed)

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
    sd=sdcard.SDCard(spi,Pin(13))

    # Create a instance of MicroPython Unix-like Virtual File System (VFS)
    # It's important to have already formatted your SD card to FAT32.
    vfs=os.VfsFat(sd)
     
    # Mount the SD card at specified directory
    os.mount(sd,sd_dir)
    
    for x in range(6) :
        # temp, humidity, pressure, lat, long, alt, time
        dataset = [98.6, 84.5, 29.74, 40.4492267, -89.0431831, 244, str(gmtime())]
        writeCsv(sd_dir, "data.csv", dataset)
        sleep(1) # Sleep for x seconds.
    
    # Read all the rows from the CSV and print them to the console.
    for row in readCsv(sd_dir, "data.csv") :
        print(row)

    # Remove all files within the directory passed in. Useful for cleaning things up during testing.
    # Comment this out if you want the files to not be deleted.
    cleanupDir(sd_dir)
    