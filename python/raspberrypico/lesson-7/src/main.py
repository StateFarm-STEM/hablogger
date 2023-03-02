from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

import time, _thread

            
if __name__ == "__main__":
    i2c = I2C(0,
            sda=Pin(16),  # assign the SDA pin to GPIO 16
            scl=Pin(17),  # assign the SCL pin to GPIO 17
            freq = 400000)
    
    oled = SSD1306_I2C(128, 64, i2c) # pixel width is 128, height is 64    

    oled.text("Hello, World!", 0, 0) # Assign text to the OLED module text object
    
    oled.show() # Display the text on the module
