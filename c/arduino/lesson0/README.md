# Lesson #0. High Altitude Balloon Project


## Objective:

- The goal of this project is to build a program that can be used by schools, community groups, youth organizations, etc. to introduce:
  - Coding and electronics skills
  - Apply concepts learned in classroom to real world problems
  - Work in small groups with mentors when possible

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
  
