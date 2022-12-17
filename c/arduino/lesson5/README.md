# Welcome to Lesson #5: Storing the data

## Working with SD card using the Arduino language

#### Pre-requisites:
- It is recommended that you have successfully completed the [blinky lights lesson](/c/arduino/lesson1/)


#### Objectives:
- Breadboard a circuit
- Read and write from the SD card that is wired up to the Arduino 


#### What you will be using:
- [Arduino IDE](https://github.com/StateFarm-STEM/hablogger/blob/main/c/arduino/lesson6/screenshots/arduino-ide.png)
- [Arduino Uno](https://github.com/StateFarm-STEM/hablogger/blob/main/c/arduino/lesson6/screenshots/arduino-uno-r3.png)
- [MicroSD Card Module](https://github.com/StateFarm-STEM/hablogger/blob/main/c/arduino/lesson6/screenshots/bmp180.png)
- [Breadboard](https://github.com/StateFarm-STEM/hablogger/blob/main/c/arduino/lesson6/screenshots/breadboard.png)
- [Wires](https://github.com/StateFarm-STEM/hablogger/blob/main/c/arduino/lesson3/screenshots/1956-02.jpg)

#### What you will be learning:
- How to connect the SD card to the Arduino using a breadboard
- How to create a new Arduino Sketch project using the SDI Library
- Write the code in the Arduino IDE and upload it to the Arduino
  - Create a file on the SD card
  - Write some data to the SD card
- Watch your code run on the Arduino using Arduino IDE's serial monitor

## Guide
Read this article  and follow the steps
- [SD Card Module with Arduino: How to Read/Write Data](https://create.arduino.cc/projecthub/electropeak/sd-card-module-with-arduino-how-to-read-write-data-37f390)
### Wiring
- **Unplug the Arduino from the computer before doing this**

### Pinout chart
Pin on SD card reader | Pin on Arduino  
------ | ------
GND   | GND  
VCC   | 5V  
MISO   | 12  
MOSI   | 11  
SCK   | 13  
CS   | 10  


<img src=https://github.com/StateFarm-STEM/hablogger/blob/main/c/arduino/lesson5/screenshots/SDCardSIDE.jpg width="500" >
<img src=https://github.com/StateFarm-STEM/hablogger/blob/main/c/arduino/lesson5/screenshots/ArduinoSdcard1.jpg width="500" >
<img src=https://github.com/StateFarm-STEM/hablogger/blob/main/c/arduino/lesson5/screenshots/ArduinoSDcard2.jpg width="500" >

- Remember you do not have to use the same color of jumper wire as this, but insure that your connections are the same. 

#### Working code to test SD card
```
#include <SPI.h>
#include <SD.h>
File myFile;
void setup() {
// Open serial communications and wait for port to open:
Serial.begin(9600);
while (!Serial) {
; // wait for serial port to connect. Needed for native USB port only
}
Serial.print("Initializing SD card...");
if (!SD.begin(10)) {
Serial.println("initialization failed!");
while (1);
}
Serial.println("initialization done.");
// open the file. note that only one file can be open at a time,
// so you have to close this one before opening another.
myFile = SD.open("test.txt", FILE_WRITE);
// if the file opened okay, write to it:
if (myFile) {
Serial.print("Writing to test.txt...");
myFile.println("This is a test file :)");
myFile.println("testing 1, 2, 3.");
for (int i = 0; i < 20; i++) {
myFile.println(i);
}
// close the file:
myFile.close();
Serial.println("done.");
} else {
// if the file didn't open, print an error:
Serial.println("error opening test.txt");
}
}
void loop() {
// nothing happens after setup
}

```


### Troubleshooting
- If using a SD card larger that 32gb partitioning down to 32gb or less and formatting to fat32 may be required
- If the SD card is not registering check all your connections first, if this doesn't work insure that the card is empty and formatted to fat 32


### Review
- Learned how to connect the SD card to the Arduino using a breadboard
- How to create a new Arduino Sketch project using the SDI Library
  - Create a file on the SD card
  - Write some data to the SD card

### [Need help?](https://github.com/StateFarm-STEM/pyinthesky#need-some-help)

