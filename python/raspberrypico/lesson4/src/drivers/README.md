# GT-U Driver for Raspberry Pi Pico

## GPS data returned from GT-U7 module

All GPS sentence data can be found at the [NMEA sentence information](http://aprs.gids.nl/nmea/) website.

|$GPXXX  | Description |
| ------ | ----------- |
| $GPGGA | Global Positioning System Fix Data. 3D location and accuracy data. |
| $GPGSA | GPS DOP and active satellites |
| $GPGSV | Detailed information of the GPS satellite |
| $GPGLL | Geographic Latitude and Longitude |
| $GPRMC | Position, velocity and time |
| $GPVTG | Dual ground/water speed |

We are interested in the GPGGA data. It returns a bytestring of 15 indexes:

`$GPGGA, 103005, 3807.038, N, 07128.99030, E, 1, 07, 1.43, 134.5, M, 42.9, M, , *78`

* `[0]` : Global Positioning System Fix Data
* `[1]` : Time (UTC HHMMSS) when the data was accessed
* `[2,3]` : Latitude 38 degrees 07.038′ N
* `[4,5]` : Longitude 71 degrees 28.00030′ E
* `[6]` : GPS fix
* `[7]` : Number of satellites being tracked
* `[8]` : Horizontal dilution of position
* `[9,10]` : Altitude (m) above the sea level
* `[11,12]` : Height of geoid (mean sea level)
* `[13]` : Time in seconds since last DGPS update
* `[14]` DGPS station ID number
* `[15]` Checksum data