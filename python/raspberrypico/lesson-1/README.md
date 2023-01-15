# hablogger
 High Altitude Balloon Data Logging Project

```python
# Blinks onboard LED every 1 second

from machine import Pin
import time

led = Pin(25, Pin.OUT)

while True:
    led.toggle()
    time.sleep(1)
```