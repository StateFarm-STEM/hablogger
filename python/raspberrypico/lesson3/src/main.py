from machine import Pin, I2C
from drivers import bmp180
import time  # the time library will enable us to use the sleep method

if __name__ == "__main__" :
    # Main entrypoint. Primary code functions start here.
    
    # Create a variable to control how long the LED will stay on, in seconds
    timerPeriod = 1

    # Initialize I2C using available I2C pins
    bus =  I2C(0,
               scl=Pin(17),
               sda=Pin(16),
               freq=100000)
    
    # Initialize BMP180 with previously defined I2C config
    bmp180 = bmp180.BMP180(bus)
    
    bmp180.oversample_sett = 2 # Accuracy, as defined in driver docs: https://github.com/micropython-IMU/micropython-bmp180
    bmp180.baseline = 101325   # Baseline pressure, as defined in driver docs: https://github.com/micropython-IMU/micropython-bmp180

    while True:
        temp = bmp180.temperature  # Capture temperature, assign to `temp` variable
        p = bmp180.pressure        # Capture pressure, assign to `p` variable
        altitude = bmp180.altitude # Capture altitude, assign to `altitude` variable
        
        # Print results to console
        print("Temperature (C):\t %d" % temp)
        print("Pressure (Pa):  \t %d" % p)
        print("Altitude (m):   \t %d" % altitude)
        print("")
        time.sleep(timerPeriod)