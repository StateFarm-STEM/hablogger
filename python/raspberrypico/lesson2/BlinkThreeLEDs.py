# Turns three LEDs on/off in sequence

from machine import Pin  # This imports the libraries needed for us to access the Pico and it's pins
import time  # the time library will enable us to use the sleep method

# Create variables for each LED, initializaing them to the pins they are connected to   
redled = Pin(13, Pin.OUT)
yellowled = Pin(14, Pin.OUT) 
greenled = Pin(15, Pin.OUT)

# Create a variable to control how long the LED will stay on, in seconds
timerPeriod = 1

while True:  # A while loop will run until the argument is no longer true.  In this case, True will always be true so it will run forever until we forcefully stop the program
    greenled.on()  # Turn the green LED on
    time.sleep(timerPeriod)  # Sleeping now will keep the LED on for the period specified by the variable you created ealier
    greenled.off()  # Turn the green LED off
    # what line of code would you add here to keep the LED off for a specified period?
    yellowled.on()  # Turn the yellow LED on
    time.sleep(timerPeriod)  
    yellowled.off()  
    redled.on()  
    time.sleep(timerPeriod) 
    redled.off()  
    time.sleep(timerPeriod)  
    
