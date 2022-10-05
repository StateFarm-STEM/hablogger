# Welcome to Lesson #2: Arduino Basics

## Arduino Basics: Blink the built-in LED on the Arduino

#### Pre-requisites:
- none

#### Objectives:
- How to download the Arduino IDE software
- How to connect to the Arduino to your computer
- Make the onboard LED blink 

## Blink the LED

#### What you will be using:
- [Arduino IDE picture](https://github.com/StateFarm-STEM/pyinthesky/blob/main/lesson4/screenshots/arduino-ide.png)
- [Link to Arduino IDE download](https://www.arduino.cc/en/software)
- [Arduino Uno](https://github.com/StateFarm-STEM/pyinthesky/blob/main/lesson4/screenshots/arduino-uno-r3.png)

#### What you will be learning:
- How to download the Arduino IDE software
- How to create a new Arduino Sketch project
- How to write the code in the Arduino IDE and upload it to the Arduino
  - blink the LED

### Guide
[Arduino basics with hands on labs](https://youtu.be/fJWR7dBuc18?t=1)

#### Helpful video shortcuts
- [Download the Arduino IDE software](https://youtu.be/fJWR7dBuc18?t=167)
- [How to connect the Arduino to your PC](https://youtu.be/fJWR7dBuc18?t=437)
- [What is a COM port?](https://youtu.be/fJWR7dBuc18?t=556)
- [Where is the onboard LED?](https://youtu.be/fJWR7dBuc18?t=715)

#### Working project
- [sketch-blink-onboard-led](https://github.com/StateFarm-STEM/pyinthesky/blob/main/my-workspace/blink-onboard-led/blink-onboard-led.ino)
```void setup() {
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
- if you are having trouble please make sure that the usb cord that came with your kit is plugged in to both the ardiuno and the pc/laptop that you are using


### [Need help?](https://github.com/StateFarm-STEM/pyinthesky#need-some-help)
