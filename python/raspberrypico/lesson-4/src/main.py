# Import all needed libraries
from machine import Pin, UART
import time
from drivers import gtu7

if __name__ == "__main__" :
    
    # Define our UART(Universal Asynchronous Receiver/Transmitter)
    uart = UART(1,
                baudrate=9600,
                timeout=3600,
                tx=Pin(4),
                rx=Pin(5))
    
    # Loop for GPS coordinates
    while True:
        gps_module = gtu7.GTU7(uart)

        gpgga_data = gps_module.gpgga()
        #print(gpgga_data)   # Uncomment this to print the "raw" data from the GPS module.
                            # If only `[]` is printed, it means no data is being received. See
                            # the Troubleshooting section for more help.

        print("Latitude:\t{0}\nLongitude:\t{1}\nSatellites:\t{2}\nTime:\t\t{3}\n".
              format(gpgga_data[1], gpgga_data[2], gpgga_data[3], gpgga_data[0]))

        time.sleep(5)
