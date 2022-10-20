# Welcome to Lesson #5: Storing the data

## Working with SD card using the Arduino language

#### Pre-requisites:
- it is recommended that you have successfully completed the [blinky lights lesson](https://github.com/StateFarm-STEM/pyinthesky/tree/main/lesson2#welcome-to-lesson-2)


#### Objectives:
- Breadboard a circuit
- Read and write from the SD card that is wired up to the Arduino 


#### What you will be using:
- [Arduino IDE](https://github.com/StateFarm-STEM/pyinthesky/blob/main/lesson6/screenshots/arduino-ide.png)
- [Arduino Uno](https://github.com/StateFarm-STEM/pyinthesky/blob/main/lesson6/screenshots/arduino-uno-r3.png)
- [MicroSD Card Module](https://github.com/StateFarm-STEM/pyinthesky/blob/main/lesson6/screenshots/bmp180.png)
- [Breadboard](https://github.com/StateFarm-STEM/pyinthesky/blob/main/lesson6/screenshots/breadboard.png)
- [Wires](https://github.com/StateFarm-STEM/pyinthesky/blob/main/lesson3/screenshots/1956-02.jpg)

#### What you will be learning:
- How to connect the SD card to the Arduino using a breadboard
- How to create a new Arduino Sketch project using the SDI Library
- Write the code in the Arduino IDE and upload it to the Arduino
  - create a file on the SD card
  - Write some data to the SD card
- Watch your code run on the Arduino using Arduino IDE's serial monitor

### Guide
[SD Card Module with Arduino: How to Read/Write Data](https://create.arduino.cc/projecthub/electropeak/sd-card-module-with-arduino-how-to-read-write-data-37f390)
### Wiring
- Here is a wiring chart
- **Unplug the Arduino from the computer before doing this**

Pin on SD card reader | Pin on Arduino  
------ | ------
GND   | GND  
VCC   | 5V  
MISO   | 12  
MOSI   | 11  
SCK   | 13  
CS   | 10  


<img src=https://github.com/StateFarm-STEM/pyinthesky/blob/main/lesson5/screenshots/SDCardSIDE.jpg width="500" >
<img src=https://github.com/StateFarm-STEM/pyinthesky/blob/main/lesson5/screenshots/ArduinoSdcard1.jpg width="500" >
<img src=https://github.com/StateFarm-STEM/pyinthesky/blob/main/lesson5/screenshots/ArduinoSDcard2.jpg width="500" >

- Remember you do not have to use the same color of jumper wire as this, but insure that your connections are the same. 

#### Working project
- [sketch-arduino-sdcard-write](https://github.com/StateFarm-STEM/pyinthesky/blob/main/my-workspace/sketch-arduino-sdcard-write/sketch-arduino-sdcard-write.ino)

### [Need help?](https://github.com/StateFarm-STEM/pyinthesky#need-some-help)
