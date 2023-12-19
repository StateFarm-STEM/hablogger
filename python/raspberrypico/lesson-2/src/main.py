from machine import Pin
import time

while True:
    for x in range(18,21):
        led = Pin(x, Pin.OUT)
        led.on()
        time.sleep(1)
        led.off()
