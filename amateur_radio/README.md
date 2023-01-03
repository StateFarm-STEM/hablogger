# Amateur Radio In This Project

## Goals
To track the High Altitude Balloon, Amateur Radio is leveraged.  There are other tracking options that do not require a license, but among the goals are:
 - Introduce Amateur Radio to students and educators
 - Introduce new types of wireless communication with hands-on learning
 - Demonstrate the benefits of Amateur Radio beyond the balloon project, such as being able to communicate during emergencies
 - Show students there are Amateur Radio scholarships available, if they obtain their license.

## Overview
Amateur Radio, also known as Ham Radio, is the use of radio communications for the purposes of non-commercial exchange of messages, wireless experimentation, self-training, private recreation, and emergency communications.

Amateur Radio is utilized by the project to track and collect real-time flight telemetry information from the High Altitude Balloon, and locating the payload after landing.  HAB tracking via Amateur Radio is performed commonly via two means:
- Automatic Packet Reporting System (APRS)
- Weak Signal Propagation Reporter (WSPR) (pronounced whisper)

Each option has benefits and limitations, depending on the types of balloon and the tracking goals.

## Automatic Packet Reporting System (APRS)

APRS is an amateur radio-based system for real time digital communication of locale information of 'immediate value'.  APRS was designed to support rapid, reliable exchange of information for local, tactical real-time decisions, events, or communication nets.  The technology was developed in the mid 1980s. It is designed to communicate all relevant information immediately to everyone (all stations and participants) to ensure the information shared is consistent.  Data can include Global Positioning System (GPS) coordinates, weather station data, text messages, announcements, queries, and other telemetry information that needs to be shared. The data sent over APRS is (often) displayed and viewed on a map, showing the position of stations, objects, tracks of moving objects, weather, and other information to assist search and rescue and direction finding.  

### APRS Messages

Information is maintained and refreshed at regular intervals. APRS uses a standard message types / formats to communicate POSITION, STATUS, MESSAGES and QUERIES, but also to accurately display map objects such as vehicles and stations.  Because it is a shared telecommunication medium (wireless RF network), guidelines on use, and how often stations should check in are defined.  For example, it is recommended stations limit how often they beacon to avoid creating unnecessary congestion for high or emergency priority messages.  Stations that need to regularly transmit position updates, it is generally recommended their beacon interval be no less than every 60 to 90 seconds.

Over the APRS network, all messages are delivered in real-time to all stations and recipients.  Messages are not stored and forwarded, but retried/relayed until time out is reached. The delivery of these messages is global, since APRS-IS distributes all packets over the internet to all other iGate repeaters in the world.  And messages will actually go back to wireless RF via any iGate that is near the intended recipent.

Below are a couple important message types:

### Telemetry Messages (Position/Object/Item)

APRS telemetry messages relay position, object, and item information containing latitude, longtitude, a symbol to be displayed on a map, and optional user fields.  These fields can include altitude, course, speed, radiated power, equipment voltage, antenna height, above average terrain, antenna gain, voice operating frequency, and more.  

For high-altitude balloon trackers, there is generally opportunity to include custom fields in telemetry messages to relay situation information about the payload and flight.  Temperature, pressure, battery voltage, and message count are common examples.  Some trackers support the ability to attach external sensors via I2C that can provide other information to relay.  The latitude and longitude coordinatres are automatically derive from GPS module included in the tracker.  

These fields along with message handling fields are encoded into a single string, which is transmitted at low power by the tracker.

**Example Telemetry Map**
(flight path image goes here)

**Example Raw Message**
```BR4XZ-10>AP51DW,WIDE1-1,WIDE2-1,qAS,BR4XZ-11:!3415.83N/11716.40ErXuZhou APRS 144.640Mhz 45W 13.8V  20.8C```

**Example External Sensor**
(bmp280 sensor image goes here)

```KW9D-11>APLIGA,N9ULL*,WIDE2-1,qAR,N9NWI-1:/151926h4032.58N/08855.34WO321/021/A=002143 00168H 30.1C 941.hPa 16.1C 945.hPa 44.9%```

### Status Messages (Comments)

APRS status messages follow a free-form format that allows each station to annouce other information that should be relayed to participants.  This information could be current mission, application, contact information, or any other information or data of immediate value surrounding the activities occuring.  Status messages can also be used for point-to-point communication, sending a message directed to a specific recipient.  

Status messages can be used by high-altitude balloon trackers to relay the school name, class, and other info about the high-altitude balloon project.  Additionally, status messages can relay health information about the tracker and equipment included in the payload.

Other uses for status messages are bulletins and announcements.  Bulletins and Announcements are treated specially by APRS and are meant to be display on a single 'community Bulletin board'.  This bulletin board is fixed size with all bulletins posted to the community, sorted for display.  The intent again is to ensure all participants are seeing the same information at the same time. 

## APRS Technical Details

APRS in its most widely used form, uses data transport over the AX.25 protocol on the 2-meter (144 Mhz to 148 Mhz) Amateur Radio band, using 1,200-bits/second Bell 202 modems.  The modems, or terminal node controllers (TNCs), generate two audio tones performing Audio Frequency Shift Keying (AFSK) to encode data, sent and received by handheld, mobile and base station radios.  For High Altitude Balloon flights, a small lightweight tracker is utilized.

Each APRS packet transmitted by a station may be received and relayed by a local digital repeater, or "digipeater".  This is especially important for mobile stations, such as those in vehicles.  In the United States, there is an extensive "digipeater" network providing transport and relay of APRS packets to ensure information is re-transmitted and received by all area participants.  Many digipeaters have Internet Gateway (iGates) connecting the on-the-air APRS with the APRS Internet System (APRS-IS) network which provides a worldwide high-bandwidth backbone for data sharing.  This allows APRS data to be shared with APRS websites, such as [APRS.fi](https://www.apfs.fi/) and others, for web-based aggregation and mapping.

## APRS Mobile Stations
The two images below should give you an idea of the kinds of information available to the operator on a APRS radio. On the left is the Kenwood D710 radio showing the station list, and on the right is the attached GPS map display showing the location of other APRS stations.

| **Raw Messages** | **GPS Map** |
| :----------: | :-----: |
| <img src="http://www.aprs.org/D7xx/AB9FXd710list1.JPG" width="450" /> | <img src="http://www.aprs.org/avmap/AVMAPg5_new_iconXx.JPG" width="500" /> |

<br/>

<details>
<summary><b>More Information</b></summary>

### APRS Frequencies Globally
Different frequencies are allocated for APRS across the globe.  For pico-balloon flights that maybe traveling across international boundaries, APRS geofencing must be supported by the tracker to ensure messages continue to be received.

![Frequencies by geographic area](http://www.aprs.org/maps/APRSVHFworldmapXx.jpg)

### APRS Digipeater PATH Relay

PATH settings determine what kind and how many digipeaters will be used to relay packets to their destination.  For all High-Altitude Balloon (HAB) and Pico-Balloon flights, WIDE-1 path settings are the guideline since multiple digipeater stations on the ground may receive APRS data transmitted.

<img src="http://www.aprs.net.au/sites/default/files/Digi-Demo.gif" />

</details>

## References


[APRS Overview and more information](http://www.aprs.org/)
[What is AFSK](https://www.notblackmagic.com/bitsnpieces/afsk//#what-is-afsk)
[2-Meter Amateur Radio Band](https://en.wikipedia.org/wiki/2-meter_band)

## Weak Signal Propagation Reporter (WSPR)

WSPR (prounced "whisper") is a protocol designed for weak-signal radio communication.  It is commonly used to by amateur radio operators for sending and recieving very low-power transmissions to test propagatino path on the Medium Frequency (MF) and High Frequency (HF) bands.  The protocol is designed and written initially by Joe Taylor (K1JT) and uses open source software developed and supported by  small team.  WSPR transmission, similiar to APRS, use a standard message format, carrying the station's call sign, Madienhead grid locator, and transmitter power in dBm.  The program decodes signals with a signal-to-noise (SNR) as low as -28 dB, with stations sending reports to online central database called WSPRnet, which includes mapping.

### References

[Weak Signal Propagation Reporter (WSPR)](https://en.wikipedia.org/wiki/WSPR_(amateur_radio_software))
[WSPR - Distant Whispers](http://www.g4ilo.com/wspr.html)
[WSPRNet](http://www.wsprnet.org/drupal/wsprnet/map)

## Tracking the balloon




## Getting your licensce

[Ham Radio School](https://www.hamradioschool.com/)


## Helpful links

[APRS.org](http://www.aprs.org/)


## Citation
