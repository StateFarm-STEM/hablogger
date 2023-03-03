# Import all needed libraries
from machine import Pin, UART
import time
from drivers import gtu7

if __name__ == "__main__" :
    
    led = Pin( #Initialize a variable called "led" as a "Pin" object
    25, #Assign pin number for onboard led (25 for Pico and "LED" for PicoW)
    Pin.OUT) #Specify this is an output pin, meaning we will send data to the pin vs recieving data from it
    
    # Define our UART(Universal Asynchronous Receiver/Transmitter)
    uart = UART(1,
                baudrate=9600,
                timeout=3600,
                tx=Pin(4),
                rx=Pin(5))
    
    # Loop for GPS coordinates and toggle the LED for action
    while True:
        led.on()
        
        gps_module = gtu7.GTU7(uart)

        gpgga_data = gps_module.gpgga()
        #print(gpgga_data)
        print("Latitude:\t{0}\nLongitude:\t{1}\nSatellites:\t{2}\nTime:\t\t{3}\n".
              format(gpgga_data[1], gpgga_data[2], gpgga_data[3], gpgga_data[0]))

        led.off()
        time.sleep(5)
