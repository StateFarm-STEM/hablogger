# Blinks an external LED

from machine import Pin  # This imports the libraries needed for us to access the Pico and it's pins
import time # the time library will enable us to use the sleep method

# The next few lines creates and initializes a variable "led" as type "Pin" with initialization parameters.  It can also be written in one line like this... led = Pin(15, Pin.OUT)
led = Pin( # Initialize a variable called "led" as a "Pin" object
    15, # Assign pin number 15 (or whichever pin you connected the LED to)
    Pin.OUT) # Specify this is an output pin, meaning we will send data to the pin vs recieving data from it

while True: # A while loop will run until the argument is no longer true.  In this case, True will always be true so it will run forever until we forcefully stop the program
    led.toggle() # call the "toggle()" function of the led object
    time.sleep(1) # call the sleep() function of the time object and pass it "1" so it sleeps for 1 second