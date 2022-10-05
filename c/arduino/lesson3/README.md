
# Welcome to Lesson #3: Weather Sensor

## Working with weather sensor data using the Arduino language

#### Pre-requisites:
- you have successfully completed the [blinky lights lesson](https://github.com/StateFarm-STEM/pyinthesky/tree/main/lesson2#welcome-to-lesson-2)
- if not, do that first

#### Objectives:
- Breadboard a circuit
- Read weather sensor data
- Print the weather sensor data to the serial port

## Measure Pressure and Temperature using the BMP180

#### What you will be using:
- [Arduino IDE](https://github.com/StateFarm-STEM/pyinthesky/blob/main/lesson4/screenshots/arduino-ide.png)
- [Arduino Uno](https://github.com/StateFarm-STEM/pyinthesky/blob/main/lesson4/screenshots/arduino-uno-r3.png)
- [BMP180 Sensor](https://github.com/StateFarm-STEM/pyinthesky/blob/main/lesson3/screenshots/bmp180.png)
- [5 pin connector](https://github.com/StateFarm-STEM/pyinthesky/blob/main/lesson4/screenshots/5-pin-connector.png)
- [Breadboard](https://github.com/StateFarm-STEM/pyinthesky/blob/main/lesson4/screenshots/breadboard.png)
- [Jumper Wires](https://github.com/StateFarm-STEM/pyinthesky/blob/main/lesson3/screenshots/1956-02.jpg)

#### Note: the BMP180 Sensor didn't detect the pressure and temp accurately until I soldered the 5 pin connector to the BMP180<br>

#### What you will be learning:
- How to connect the BMP180 to the Arduino using a breadboard
- How to create a new Arduino Sketch project using the Adafruit BMP085 Library
- Write the code in the Arduino IDE and upload it to the Arduino
  - measure the temperature in Celsius from the BMP180 and convert to Fahrenheit
  - read the pressure in pascals and convert to inches of mercury
  - print your calculations to the Arduino's serial port
- Watch your code run on the Arduino using Arduino IDE's serial monitor

### Guide
[Python with Arduino LESSON 9 Measuring Pressure and Temperature with the BMP180 Sensor](https://toptechboy.com/python-with-arduino-lesson-9-measuring-pressure-and-temperature-with-the-bmp180-sensor/)

### Wiring help
 <img src="https://github.com/StateFarm-STEM/pyinthesky/blob/main/lesson3/screenshots/BMP_BACKWIRE.jpg" width="500" >
 <img src="https://github.com/StateFarm-STEM/pyinthesky/blob/main/lesson3/screenshots/BMPWIRE2.jpg" width="500" >

- Remember that you don't have to use the same color wires I do, but make sure they connect the same way. 


Connecting Up the BMP180 Pressure and Temperature Sensor
| BMP180 Pin | Arduino Pin |
| -------------- | :--------- | 
Vin |	5V
GND	| GND
SCL	| A5
SDA	| A4
#### Helpful video shortcuts
- [connect the BMP180 to the Arduino](https://youtu.be/z9AzZM1-Dns?t=105)
- [how to add the Adafruit Library to the Arduino IDE](https://youtu.be/z9AzZM1-Dns?t=152)
- [write the code and run it on the Arduino](https://youtu.be/z9AzZM1-Dns?t=396)
- [convert pascals to inches of mercury](https://youtu.be/z9AzZM1-Dns?t=985)
### Tips
- the color of the wires do not matter as long as they are connected to the right pins
- make sure that you have the librarys installed [found here](https://learn.adafruit.com/bmp085/using-the-bmp085)



### Trouble shooting
- if you get an error code that looks like this `fatal error: Adafruit_I2CDevice.h` you are missing the BusIO library, follow [this guide](https://www.chippiko.com/ii2cdevice-no-such-file) to solve this issue
- After you run the code if you don't see data, make sure to open your serial monitor. ctrl + shift + m or enter the tools menu and select the serial monitor. 
- if you get in error like this one <code>Error opening serial port 'COM3'. (Port not found)
</code> while attempting to open your serial monitor, insure that your Arduino is still plugged in and everything is wired correctly

#### Working Code - if you get stuck click copy and paste the code into your sketch

```
//#include <SD.h> // load the SD library
//#include <SPI.h> // load the SPI library

#include "Wire.h"    // imports the wire library for talking over I2C 
#include "Adafruit_BMP085.h"  // import the Pressure Sensor Library
Adafruit_BMP085 mySensor;  // create sensor object called mySensor

float tempC;  // Variable for holding temp in C
float tempF;  // Variable for holding temp in F
float pressure; //Variable for holding pressure reading

void setup(){
  Serial.begin(9600); //turn on serial monitor
  mySensor.begin();   //initialize mySensor
}



void loop() {
  tempC = mySensor.readTemperature(); //  Read Temperature
  tempF = tempC*1.8 + 32.; // Convert degrees C to F
  pressure=mySensor.readPressure(); //Read Pressure
  
  Serial.print("The Temp is: "); //Print Your results
  Serial.print(tempF);
  Serial.println(" degrees in F (fahrenheit)");
  Serial.print("The Pressure is: ");
  Serial.print(pressure/3386.389);
  Serial.println(" in of HG (inches of mercury).");
  Serial.println("");
  delay(250); //Pause between readings.
}
```
### [Need help?](https://github.com/StateFarm-STEM/pyinthesky#need-some-help)
