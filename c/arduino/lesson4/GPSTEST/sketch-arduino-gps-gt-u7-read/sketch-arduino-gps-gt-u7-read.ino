#include "TinyGPSPlus.h"
#include <SoftwareSerial.h>

// Create the serial_connection
//
// Connect the GT-U7 RX and TX to the Arduino
// using the following connections...
// RX=pin --> Arduino analog 10
// TX pin --> Arduino analog 11
//
// In the code below on line 14 is the constructor.
// use the TX pin number as the first argument
// use the RX pin number as the second argument
SoftwareSerial serial_connection(11, 10);

TinyGPSPlus gps;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  serial_connection.begin(9600);
  Serial.println("GPS Start");
}

void loop() {
  // put your main code here, to run repeatedly:
  while(serial_connection.available())
  {
    gps.encode(serial_connection.read());
  }
  if(gps.location.isUpdated())
  {
    Serial.println("Satellite Count:");
    Serial.println(gps.satellites.value());
    Serial.println("Latitude:");
    Serial.println(gps.location.lat(), 6);
    Serial.println("Longitude:");
    Serial.println(gps.location.lng(), 6);
    Serial.println("Speed MPH:");
    Serial.println(gps.speed.mph());
    Serial.println("Altitude Feet:");
    Serial.println(gps.altitude.feet());
    Serial.println("");
  }
}
