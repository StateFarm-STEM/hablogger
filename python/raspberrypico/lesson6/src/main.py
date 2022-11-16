from machine import Pin, SPI, Timer, I2C
from drivers import sdcard
from drivers import bmp180 as bmp180driver
from time import sleep, gmtime

import os


def blinkLed(timer_one) :   
    led.toggle()


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

def getDataBmp180(bmp180) :
    temp = bmp180.temperature  # Capture temperature, assign to `temp` variable
    p = bmp180.pressure        # Capture pressure, assign to `p` variable
    altitude = bmp180.altitude # Capture altitude, assign to `altitude` variable

    return [temp, p, altitude]

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

    vfs=os.VfsFat(sd)
     
    os.mount(sd,sd_dir)

def writeCsv(sd_dir, file_name, dataset) :
    # print("Writing data to '%s/%s'..." % (sd_dir, file_name))
    with open(sd_dir + '/' + file_name,'a+') as csv_out :
        for data in dataset :
            if data == dataset[-1] :
                csv_out.write('"'+str(data)+'"')
            else :
                csv_out.write('"'+str(data)+'",')
        csv_out.write('\n')
    print("Done.")


def readCsv(sd_dir, file_name) :
    csv_data = []
    # print("Reading data from '%s/%s'..." % (sd_dir, file_name))
    with open(sd_dir + '/' + file_name,'r') as csv_in :
        for line in csv_in:
            line=line.rstrip('\n')
            line=line.rstrip('\r')
            csv_data.append(line.split(','))
    print("Done")

    return csv_data


def cleanupDir(rmdir) :
    print("Deleting files from '%s'..." % rmdir)
    for file in os.listdir(rmdir)[1:] :
        os.remove(rmdir + '/' + file)
    print("Done.")


if __name__ == "__main__" :   
    led = Pin(25, Pin.OUT)  # Assign on board LED to variable
    sd_dir = '/sd'          # Directory created on SD card at root '/'. Expected format is '/<string>'. Example: '/sd'
        
    machine.Timer().init(freq=1, mode=Timer.PERIODIC, callback=blinkLed)

    initSDCard(sd_dir)
    bmp180 = initBmp180()

    bmp_data = getDataBmp180(bmp180)

    # print(bmp_data)

    writeCsv(sd_dir, "data.csv", bmp_data)
    
    # Read all the rows from the CSV and print them to the console.
    for row in readCsv(sd_dir, "data.csv") :
        print(row)

    # cleanupDir(sd_dir)
    

