# High altitude Balloon (HAB) Logger

HABLogger is a project built to be usable by schools, community groups, youth organizations, and more as an introduction to programming, electronics and team building.

The [National Weather Service](https://www.weather.gov/chs/upperair) launches a minimum of two high altitude balloons a day from [91 locations](https://www.weather.gov/upperair/nws_upper) at 1100 and 2300 UTC to observe weather conditions used to model weather forecasts. When flying high altitude ballons, data is usually collected throughout the flight and later retrieved for analysis.

This project contains lessons wherein learners will launch their own weather balloon to the stratosphere, or approximately 90,000+ feet. Throughout the balloon flight, the components within the payload will collect temperature, barometric pressure, latitude, longitude, elevation, and other telemetry data. This information is collected via the peripheral modules attached to the microcontrollers within the payload and stored in an SD card for analysis after recovery.

The project contains basic hands-on experiences with the following:

- Microcontrollers & electronics, including wiring peripheral modules between a microcontroller and breadboard
- Programming microcontrollers to interact with peripheral modules using C programming language (Arduino microcontroller) or Python (Raspberry Pi Pico microcontroller)
- Launching a finished product in a high-altitude balloon flight to the stratosphere (90,000+ feet)
- Analyzing collected data after recovering the balloon payload

Each lesson is constructed to be completed within the timeframe of a typical classroom experience (approximately 45 minutes to 1 hour), and are designed to be completed by small groups (between 2 and 5 learners is recommended)

## Lesson Overview

- Lesson 1: Introduction and how to get started
  - Details about high altitude balloons
  - Introduction to electronics and components used in the project
  - Installing and using the preferred integrated development enviornment (IDE)
- Lesson 2: Blinking lights
  - Traditional first project with microcontrollers getting students comfortable with breadboards, components, microcontrollers, and loading code to the device 
- Lesson 3: Working with the weather sensor
  - Wiring up sensors to read temperature and barometric pressure
- Lesson 4: Working with the GPS module
  - Wiring up GPS hardware to the microcontroller and reading satellite telemetry
- Lesson 5: Working with the SD card module
  - Wire up SD card hardware then writing and reading contents from the SD card
- Lesson 6: Putting it all together
  - Wire everything up and write telemetry data to SD card
  - Read telemetry data from the SD card
- Analyzing telemetry and log data
  - Samples to interpret flight data

### Accessing the Lessons

The content is divided up by language and within the language you can choose the platform (where applicable).
- [C](https://github.com/StateFarm-STEM/hablogger/tree/main/c)
- [Python](https://github.com/StateFarm-STEM/hablogger/tree/main/python)


# Need Help?

- Report an issue by clicking the [issue](https://github.com/StateFarm-STEM/hablogger/issues) link towards the top of the page
