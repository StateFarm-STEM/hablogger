# Blinks an external LED

from machine import Pin, Timer # This imports the libraries "Pin" and "Timer" needed for us to access the Pico, it's pins, and the Timer object

# The next few lines creates and initializes a variable "led" as type "Pin" with initialization parameters.  It can also be written in one line like this... led = Pin(15, Pin.OUT)
led = Pin(  # Create a variable "led" as type "Pin" 
    15,  # Assign pin number 15 (or whichever pin you connected the LED to)
    Pin.OUT) # Specify this is an output pin, meaning we will send data to the pin vs recieving data from it

timer = Timer() # Create a variable called "timer" of time "Timer"
timerPeriod = 1000  # Create a variable "timerPeriod" and initialize it to 1000 (or however long you want the LED to stay on, in miliseconds)

def blink(timer):  # Define a function called "blink" with an input parameter called "timer" that will be used to toggle the LED on/off
    led.toggle()  # Call the "toggle()" function within the led object, which was earlier defined as type "Pin"

# start the timer running
timer.init(  
    mode = Timer.PERIODIC, # The "mode" parameter being set to PERIODIC will run the timer in an interval defind by the "period" parameter 
    period = timerPeriod,  # The "period" parameter indicates the frequency the timer will run (in milisecons), here you are passing in the "timerPeriod" variable you created earlier
    callback = blink)  # The "callback" parameter indicates the function that should be called each time the timer is run, here you are passing the "blink" function you created earlier
