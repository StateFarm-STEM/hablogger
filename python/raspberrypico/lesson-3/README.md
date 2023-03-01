# Lesson 3: Temperature, Pressure, and Altitude
## High Altitude Balloon Data Logging

### Pre-requisites
* Complete [Lesson 1: Blinking Light](../lesson1/README.md)
* [Thonny Python IDE](https://thonny.org/) installed on your computer
* All necessary hardware components (Raspberry Pi Pico, BPM-180 module, breadboard, wires, USB cable, computer)

### Objectives
* Use breadboard to wire BMP-180 module to Raspberry Pi Pico
* Install the BPM-180 MicroPython driver to the Raspberry Pi Pico
* Print temperature, pressure, and altitude to the console

### Results
* Familiarity with wiring a breadboard
* Understanding of basic MicroPython code
* Learn the importance of MicroPython drivers and how to use them
* A functioning program for reading temperature, pressure, and altitude using the BMP-180<br><br>

### Video Walk-through
In addition to the reading below, you can watch this [video](videos/Lesson3.mp4?raw=true) for guidance!
<br><br>

## Steps

  **IMPORTANT** Before wiring your Pico, UNPLUG IT FROM YOUR COMPUTER. If plugged in while wiring, you risk damaging the Pico or BMP-180 module.

1. Wire the BMP-180 to the Raspberry Pi Pico.
    BMP-180 Pins | Description | Pi Pico Pins
    ------------ | ----------- | ------------
    VIN          | (Voltage In): Provides power to the BMP-180. Connect to the 5V pin on Pico | 5V (40)
    GND          | (Ground): Connect to the ground pin on Pico | GND (38)
    SCL          | (Serial Clock): Accepts clock pulses from the Pico to synchronize data transmission | GP17 (22)
    SDA          | (Serial Data): Used for data exchange | GP16 (21)

    ![bmp-180-diagram](./docs/pi-pico-bmp180.png)

    ![Lesson Three](./docs/lesson3.jpg)

### Install BMP-180 Driver

Drivers are code modules for enabling certain functionality. One such driver allows us to read data from the BMP-180 module. This driver is called `bmp180.py` and is located in the [../drivers/src/bmp180.py](../drivers/src/bmp180.py) location. The following steps will result in saving this driver to the Raspberry Pi Pico so the driver can be used by our Python code.

1. Download the driver called `bmp180.py` located in the [../drivers/src/bmp180.py](../drivers/src/bmp180.py) location.

1. Connect your Raspberry Pi Pico to your computer using the USB cable.

1. Open the Thonny IDE. _Stop/Restart_ the backend to refresh the connection.

    ![stop-restart](./docs/thonny-1.png)

    You should now see `Raspberry Pi Pico` displayed in the left-hand navigation of Thonny. If the "Files" window is not displaying add it from the View > Files menu.

    ![files-menu](./docs/FilesView.jpg)

1. If one does not already exist, create a new directory in Thonny on the Raspberry Pi Pic called `drivers`.
    
    ![drivers-directory](./docs/thonny-2.png)

1. Using Thonny, select _File_ then _Open_ from the menu. Choose _This Computer_. Navigate to the location where you downloaded `bmp180.py` in a previous step. Select the file and click _Open_.

1. Save the `bmp180.py` file to the Raspberry Pi Pico. This allows our code to use the driver to perform BMP-180 actions in MicroPython when running on the Pi Pico. 

    Click _File_ then _Save as..._. Choose _Raspberry Pi Pico_. Double-click the `drivers` folder created in a previous step. Then save the `bmp180.py` file being sure to name it `bmp180.py`.

1. If a file called `__init__.py` does not already exist in the `/drivers` folder, create a new file in Thonny called `__init__.py`. 

    Click _File_ then _New_. Then click _File_ then _Save as..._. Choose _Raspberry Pi Pico_ and save this empty file to the same `drivers` location as the previous step. Name the file `__init__.py`. This empty file is used by Python to indicate the `drivers` folder is to be used for Python modules.

    Your finished folders and files should look like this:<br>
    ![files-menu](./docs/FinishedFiles.png)

### BMP-180 Program

The steps in this section will use the previous hardware and driver sections to allow reading temperature, pressure, and altitude from the BMP-180 module. The code example for this lesson is located in [./src/main.py](./src/main.py).

1. Using Thonny, open the `main.py` file in [./src/main.py](./src/main.py).

1. Run the script.

    ![run-script](./docs/thonny-3.png)

    Output will be generated to the console in Thonny describing the actions being taken. You will see output for the temperature, pressure, and altutide captured by the BMP-180.

    Example output:

    ```
    Temperature (C):	 21
    Pressure (Pa):  	 98420
    Altitude (m):   	 232
    ```

**Congratulations! You have successfully completed Lesson 3.**
<br><br>

## Want more?
If you have finished with the base lesson, check out the items below.
<br><br>

Update the code to do any/all of the following:
1. Add the units to the end of the output
1. Convert the temperature to degrees Fahrenheit (or Kelvin 🥶)
1. Convert the pressure to inches of mercury or atmospheres
1. Convert the altitude to feet (or furlongs 🤔)
1. Create a function for unit conversions to pass variables and print output.

Things to think about, validate, and/or try:
* How can you change the temperature surrounding the BMP180 (Don't touch it 😅)
* What should the pressure reading be?
* Is the altitude correct? 
* How sensitive is the reading?
<br><br>

## Troubleshooting

* `ERROR: No module named (drivers, bmp180, ...)`
    
    If you see this error it means Python is not able to locate a module to be imported. This can occur because the version of MicroPyhon you are using does not support the module you are trying to import. Specifically for this lesson it likely applies to the `drivers` step. Ensure the `drivers` folder and its contents, `bmp180.py` and `__init__.py`, are saved to the Raspberry Pi Pico device and _not_ your computer.

    Example error message:
    ```sh
    Traceback (most recent call last):
      File "<stdin>", line 2, in <module>
    ImportError: no module named 'drivers'
    ```

## Reference Material
* [Raspberry Pi Pico Pinout](https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf)
* [Raspberry Pi Pico SDK](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf)
* [MicroPython-IMU BMP-180 Driver source code](https://github.com/micropython-IMU/micropython-bmp180)
<br><br>

## Need help?
Watch the walk-through [video](videos/Lesson3.mp4?raw=true) for guidance!
