# Lesson #1. Introduction and how to get started


## Objective:

- When flying high altitude balloon data is usually collected through the flight for later analysis. 
- The [National Weather Service](https://www.weather.gov/chs/upperair) launches a minimum of two high altitude balloons a day from [91 locations](https://www.weather.gov/upperair/nws_upper) every day at 1100 and 2300 UTC to observe weather conditions used to model weather forecasts.
- This project will launch their own weather balloon to the stratosphere or approximately 90,000+ feet.
  - Students will be responsible for tracking the following weather data:
    - Temperature around the balloon as it ascends 
    - Barometric pressure of the atmosphere at different altitudes 

  - Students will be recording the position of the balloon:
    - Latitude is recorded to map the flight path of the balloon
    - Longitude in conjunction with latitude we can plot the balloon’s location on a map 
    - Elevation is recorded for students to see how different factors can influence rate of ascent, peak elevation, etc. 
  - Students will be [saving the data](https://create.arduino.cc/projecthub/electropeak/sd-card-module-with-arduino-how-to-read-write-data-37f390) in a [CSV file](https://en.wikipedia.org/wiki/Comma-separated_values) in a micro-SD card on the tracker in the following format every 30 seconds of the flight for later analysis:
    - time, latitude, longitude, altitude, temperature, humidity, pressure
  
- To build and test this students will be using:
  - ### [Arduino Uno](https://store.arduino.cc/products/arduino-uno-rev3)
  - This is a microcontroller. It is used to run code that stores data gathered from the onboard sensors.
    - ![Arduino UNO](https://github.com/StateFarm-STEM/pyinthesky/blob/main/lesson1/photos/arduino_uno.jpg)
  - ### [Breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard/all)
  -  This is used to prototype wiring and test to make sure things work before committing to soldering components together.
    - ![Breadboard](https://github.com/StateFarm-STEM/pyinthesky/blob/main/lesson1/photos/breadboard.jpg)
  - ### [BMP-180 - Barometric Pressure/Temperature/Altitude Sensor](https://www.adafruit.com/product/1603)
  - This is used to get the barometric pressure, and the temperature of the air surrounding it, as well as the altitude that the sensor is at. This data is recorded every 30 seconds to the micro-SD card
    - <img src=https://github.com/StateFarm-STEM/pyinthesky/blob/main/lesson1/photos/BMP_both.jpg width="1000" >
  - ### [GPS Module](https://www.u-blox.com/en/product/neo-6-series)
  - This is how the balloon determines its latitude and longitude. The Arduino tells the GPS module to record its position every 30 seconds to the micro-SD card.
    - ![GPS NEO-6M](https://github.com/StateFarm-STEM/pyinthesky/blob/main/lesson1/photos/GPS_NEO-6M.JPG)
  - ### [Arduino SD card adapter](https://electropeak.com/micro-sd-tf-card-adapter-module)
  - This is how the micro-SD card is used by the Arduino to record data. It takes the data that the Arduino is giving it and writes it onto the micro-SD card.
    - ![SD Card Adapter](https://github.com/StateFarm-STEM/pyinthesky/blob/main/lesson1/photos/sd_card_module.jpg)
    
  - ### [Micro SD card](https://en.wikipedia.org/wiki/SD_card)
  - This stores all the data so you can access it later. 
  
  
# Basic guide to electronics safety 
 - While working with any type of electronics, in this case an Arduino, make sure that the surface that you are working on is not conductive. Some examples of suitable materials to work on are plastic tables or wooden tables. Stay away from any metal surfaces so you do not short the components that you are working on.
 - In this lesson breadboards will be used rather frequently. In order to safely use a breadboard a couple of concepts must be understood. 
    - First of all, what is a breadboard:
      - a breadboard is a piece of plastic with conductive material layered in channels in order to protype circuits without having to solder anything
      - There are three main parts to a bread board, the power rails, the terminal strips, and the DIP support channel.
      - The DIP support channel is the channel that runs through the middle of the board. It splits the terminal strips into two and makes it so many different integrated circuits can be used while taking up minimum space on the breadboard. Each pin of the IC (integrated circuit) is unique and needs to be separate from the other pins, hence the need for a channel that breaks up the terminal strips. 
      - Terminal strips are the strips of metal that connect the rows of pins, they are hidden, but important. This means that all of the holes on either side of the DIP channel are connected to each other. 
      - The power rails are typically accompanied by a blue or red line. These are used to provide a power source and a common ground. Blue means negative or ground and red means positive or power.
      <img src=https://github.com/StateFarm-STEM/pyinthesky/blob/main/lesson1/photos/HabBreadboard.jpg width="600" >     
    - The red and blue arrows are pointing to the positive and negative power rails respectively. The yellow arrow is illustrating which pin are connected. The pins are connected in the same direction as the yellow arrow, but separated by the channel in the middle. They are connected horizontally and not vertically in this picture. 
    - If you want more information on breadboards please refer to <a href=https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard/all title="How to Use a Breadboard">This article</a>
  - Another thing that is important to keep in mind is polarity:
     - electronics only work one way, if you connect the positive wire to the negative terminal, and the negative wire to the positive terminal, you may ruin the component you are working with.
     - in order to prevent this ***unplug the Arduino while you are wiring components and always double check that it is correct according to the picture/pinout chart***
