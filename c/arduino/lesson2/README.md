# Welcome to Lesson #2: Arduino Basics

## Arduino Basics: Blink the built-in LED on the Arduino

#### Pre-requisites:
- None

#### Objectives:
- How to download the Arduino IDE software
- How to connect to the Arduino to your computer
- Make the onboard LED blink 

### Parts required:
- Arduino 

![Arduino Uno](https://github.com/StateFarm-STEM/hablogger/blob/main/c/arduino/lesson4/screenshots/arduino-uno-r3.png)
- PC or laptop, in the guide below we will be downloading the Arduino IDE

![Arduino IDE picture](https://github.com/StateFarm-STEM/hablogger/blob/main/c/arduino/lesson4/screenshots/arduino-ide.png)
 )

### What you will be learning:
- How to download the Arduino IDE software
- How to create a new Arduino Sketch project
- How to write code in the Arduino IDE and upload it to the Arduino in order to blink the LED

## Guide
Click this link and watch the YouTube video [Arduino basics with hands on labs](https://youtu.be/fJWR7dBuc18?t=1)

#### Helpful video shortcuts
- [Downloading the Arduino IDE software](https://youtu.be/fJWR7dBuc18?t=167)
- [How to connect the Arduino to your PC](https://youtu.be/fJWR7dBuc18?t=437)
- [What is a COM port?](https://youtu.be/fJWR7dBuc18?t=556)
- [Where is the onboard LED?](https://youtu.be/fJWR7dBuc18?t=715)

#### Working project
- Copy and paste this code into your sketch
```
void setup() {
  // put your setup code here, to run once:
  pinMode(13,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(13,HIGH);
  delay(100);
  digitalWrite(13,LOW); 
  delay(900);
}
```
- If you are having trouble make sure that the USB cord is plugged in to both the Arduino and the pc/laptop that you are using


### Need help?
Watch the walkthrough video for guidence
[![Watch the video](videos/Lesson2.jpg)](videos/Lesson2.mp4)
