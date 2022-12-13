
# Welcome to Lesson #3: Weather Sensor

## Working with weather sensor data using the Arduino language

#### Pre-requisites:
- It is recommended that you have successfully completed the [blinky lights lesson](/c/arduino/lesson1/)


#### Objectives:
- Breadboard a circuit
- Read weather sensor data
- Print the weather sensor data to the serial port



#### What you will be using:
- [Arduino IDE](https://github.com/StateFarm-STEM/hablogger/blob/main/c/arduino/lesson4/screenshots/arduino-ide.png)
- [Arduino Uno](https://github.com/StateFarm-STEM/hablogger/blob/main/c/arduino/lesson4/screenshots/arduino-uno-r3.png)
- [BMP180 Sensor](https://github.com/StateFarm-STEM/hablogger/blob/main/c/arduino/lesson3/screenshots/bmp180.png)
- [5 pin connector](https://github.com/StateFarm-STEM/hablogger/blob/main/c/arduino/lesson4/screenshots/5-pin-connector.png)
- [Breadboard](https://github.com/StateFarm-STEM/hablogger/blob/main/c/arduino/lesson4/screenshots/breadboard.png)
- [Jumper Wires](https://github.com/StateFarm-STEM/hablogger/blob/main/c/arduino/lesson3/screenshots/1956-02.jpg)

#### Note: the BMP180 Sensor didn't detect the pressure and temp accurately until I soldered the 5 pin connector to the BMP180<br>

#### What you will be learning:
- How to connect the BMP180 to the Arduino using a breadboard
- How to create a new Arduino Sketch project using the Adafruit BMP085 Library
- Write the code in the Arduino IDE and upload it to the Arduino
  - Measure the temperature in Celsius from the BMP180 and convert to Fahrenheit
  - Read the pressure in pascals and convert to inches of mercury
  - Print your calculations to the Arduino's serial port
- Watch your code run on the Arduino using Arduino IDE's serial monitor

## Guide
[Python with Arduino LESSON 9 Measuring Pressure and Temperature with the BMP180 Sensor](https://toptechboy.com/python-with-arduino-lesson-9-measuring-pressure-and-temperature-with-the-bmp180-sensor/)
#### Helpful video shortcuts
- [Connect the BMP180 to the Arduino](https://youtu.be/z9AzZM1-Dns?t=105)
- [How to add the Adafruit Library to the Arduino IDE](https://youtu.be/z9AzZM1-Dns?t=152)
- [Write the code and run it on the Arduino](https://youtu.be/z9AzZM1-Dns?t=396)
- [Convert pascals to inches of mercury](https://youtu.be/z9AzZM1-Dns?t=985)
### Connecting Up the BMP180 Pressure and Temperature Sensor
**Unplug the Arduino from the computer before doing this**

 <img src=https://github.com/StateFarm-STEM/pyinthesky/blob/main/lesson3/screenshots/BMP_BACKWIRE.jpg width="500" >
 <img src=https://github.com/StateFarm-STEM/pyinthesky/blob/main/lesson3/screenshots/BMPWIRE2.jpg width="500" >
 
### Pinout chart

| BMP180 Pin | Arduino Pin |
| -------------- | :--------- | 
Vin |	5V
GND	| GND
SCL	| A5
SDA	| A4

### Tips
- The color of the wires do not matter as long as they are connected to the right pins
- Make sure that you have the libraries installed
  - Install the Adafruit BMP085 library through the Arduino IDE by going to Sketch -> Include Library -> Manage Libraries -> then search for "Adafruit bmp085 library"
  - Install the BusIO library through the Arduino IDE by going to Sketch -> Include Library -> Manage Libraries -> then search for "BusIO"
  - If that doesn't work, you can install the BMP library [found here](https://learn.adafruit.com/bmp085/using-the-bmp085)
- In order to see the serial monitor, where your data will be printing out, press ctrl + shift + m or enter the tools menu and select the serial monitor




#### Working Code 

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




### Trouble shooting
- If you get an error code that looks like this `fatal error: Adafruit_I2CDevice.h` you are are likley missing the BusIO library, to check to see if it is installed go to Sketch -> Include Library -> Manage Libraries -> then search for "BusIO", this should be installed. 
- If you get in error like this one <code>Error opening serial port 'COM3'. (Port not found)
</code> while attempting to open your serial monitor, insure that your Arduino is still plugged in and everything is wired correctly


### Reveiw
- Learned how to connect the BMP180 to the Arduino using a breadboard in order to gather data such as pressure
- Learned How to create a new Arduino Sketch project using the Adafruit BMP085 Library
  - Measure the temperature in Celsius from the BMP180 and convert to Fahrenheit
  - Read the pressure in pascals and convert to inches of mercury
  - Print your calculations to the Arduino's serial port

### [Need help?](https://github.com/StateFarm-STEM/hablogger#Needsomehelp?)
