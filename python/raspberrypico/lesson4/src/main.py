from machine import Pin, UART

from drivers import gtu7

if __name__ == "__main__" :
    

    uart = UART(1,
                baudrate=9600,
                timeout=3600,
                tx=Pin(4),
                rx=Pin(5))
    
    gps_module = gtu7.GTU7(uart)

    gpgga_data = gps_module.gpgga()
    print(gpgga_data)

    gprmc_data = gps_module.gprmc()
    print(gprmc_data)
