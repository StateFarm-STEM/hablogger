from machine import Pin, SPI, Timer
from drivers import sdcard
from time import sleep, gmtime

import os


def blinkLED(timer_one) :
    # Toggle LED functionality
    led.toggle()
    
def writeCsv(sd_dir, file_name, dataset) :
    # Write array dataset to CSV. If the file doesn't exist, create it. Otherwise, append.
    with open(sd_dir+'/'+file_name,'a+') as csv_out :
        for data in dataset :
            if data == dataset[-1] :
                # If last element in the dataset, don't add a comma.
                csv_out.write('"'+str(data)+'"')
            else :
                csv_out.write('"'+str(data)+'",')
        csv_out.write('\n')

def readCsv(sd_dir, file_name) :
    # This approach to reading a CSV bypasses the need to import the CSV package, saving on space.
    # Reading data is as as simple as referencing csv_data as an array data type. Example: csv_in[0][1]
    csv_data = []
    with open(sd_dir+'/'+file_name,'r') as csv_in :
        for line in csv_in:
            line=line.rstrip('\n')
            line=line.rstrip('\r')
            csv_data.append(line.split(','))
    return csv_data
            
def writeTextExample(sd_dir) :
    # Create / Open a CSV file in write mode. Write, 'w', mode creates a new file.
    # This example opens a file, writes text, closes the file. Then opens the same file and appends
    # a line to the bottom, thus demonstrating open/close/write features.
    
    # If the file already exists, this will overwrite it.
    file = open(sd_dir+'/example.txt','w')

    # Write sample text
    for i in range(20):
        file.write("Sample text = %s\r\n" % i)
        
    # Close the file
    file.close()

    # Open the file again and append, 'a', text. Then close the file.
    file = open(sd_dir+'/example.txt','a')
    file.write("Appended Sample Text at the END \n")
    file.close()
            
def readTextExample(sd_dir) :
    # Read, 'r', the file and print the text on debug port.
    file = open(sd_dir+'/example.txt', 'r')
    if file != 0:
        print("Reading from SD card")
        read_data = file.read()
        print (read_data)
    file.close()
    
if __name__ == "__main__" :    
    led = Pin(25, Pin.OUT)      # Assign on board LED to variable
    sd_dir = '/sd'             # Directory created on SD card at root '/'. Expected format is '/<string>'. Example: '/sd'
        
    # Initialize timer_one. Used for toggling the on board LED
    timer_one = machine.Timer()
    # Blink the onboard LED until control interrupt
    timer_one.init(freq=1, mode=Timer.PERIODIC, callback=blinkLED)

    # Intialize SPI peripheral
    spi = machine.SPI(1,
                      baudrate=1000000, # 1 MHz
                      polarity=0,
                      phase=0,
                      bits=8,
                      firstbit=SPI.MSB,
                      sck=machine.Pin(10),
                      mosi=machine.Pin(11),
                      miso=machine.Pin(12))

    # Initialize the SD card on chip select (CS) pin 13
    sd=sdcard.SDCard(spi,Pin(13))

    # Create a instance of MicroPython Unix-like Virtual File System (VFS)
    # It's important to have already formatted your SD card to FAT32.
    vfs=os.VfsFat(sd)
     
    # Mount the SD card at specified directory
    os.mount(sd,sd_dir)
    
    
    for x in range(6) :
        # temp, humidity, pressure, lat, long, alt, time
        dataset = [98.7, 84.5, 29.74, 40.4492267, -89.0431831, 244, str(gmtime())]
        writeCsv(sd_dir, "data.csv", dataset)
        sleep(2)
    
    for line in readCsv(sd_dir, "data.csv") :
        print(line)
    
    
    #writeTextExample(sd_dir)
    #readTextExample(sd_dir)

    # Debug print SD card directory and files. Uncomment this to list files in the `/sd` directory.
    # print(os.listdir(sd_dir))



