from machine import Pin, UART

from drivers import gtu7

if __name__ == "__main__" :

    uart = UART(1,
                baudrate=9600,
                tx=Pin(4),
                rx=Pin(5))

    gps_module = gtu7.GTU7(uart)
    
    while True :
        try :
            gps_data = gps_module.get_gps_data()
            
            print("Latitude: \t %s" % gps_data[0])
            print("Longitude: \t %s" % gps_data[1])
            print("Satellites: \t %d" % gps_data[2])
            print("Time:\t\t %s \n" % gps_data[3])
            
        except Exception as e :
            print("No GPS data returned.\n")
