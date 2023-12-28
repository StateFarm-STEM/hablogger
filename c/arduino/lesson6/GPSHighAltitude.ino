/*
  SD card datalogger

  This example shows how to log data from three analog sensors
  to an SD card using the SD library.

  The circuit:
   analog sensors on analog ins 0, 1, and 2
   SD card attached to SPI bus as follows:
 ** MOSI - pin 11
 ** MISO - pin 12
 ** CLK - pin 13
 ** CS - pin 10 (for MKRZero SD: SDCARD_SS_PIN)

  created  24 Nov 2010
  modified 9 Apr 2012
  by Tom Igoe

  This example code is in the public domain.

*/

#include <SPI.h>
#include <SD.h>
#include "Adafruit_BMP085.h"
#include <TinyGPS++.h>
#include <SoftwareSerial.h>

const int chipSelect = 10;
const bool bypassGPS = true;

static const int RXPin = 4, TXPin = 3;
static const uint32_t GPSBaud = 9600;
TinyGPSPlus gps;

// map software serial to gps
SoftwareSerial serialgps(TXPin, RXPin);

Adafruit_BMP085 bmp;

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  delay(1000);


  Serial.print("initializing sd card...");

  // see if the card is present and can be initialized:
  if (!SD.begin(chipSelect)) {
    Serial.println("SD Init Failed");
    // don't do anything more:
    while (1);
  }
  Serial.println("Initialized");
  // see if the card is present and can be initialized:
  if (!SD.begin(chipSelect)) {
    Serial.println("failed");
    // don't do anything more:
    while (1);
  }
  Serial.println("initialized");

  initBMP();
  initGPS();
}


void loop() {
  
  // make a string for assembling the data to log:
  String dataString = "";
  bool gpsready = false;

  unsigned long start = millis();
  do
  {
    while (serialgps.available()>0) {
      char c;
      c=serialgps.read();
      gps.encode(c);
    }
  } while (millis() - start < 5000);

  float c = bmp.readTemperature();  // Variable for holding temp in C
  float f = c*1.8 + 32.;  // Variable for holding temp in F
  // //float pressure = bmp.readPressure()/3386.3887; //pascals to in of mercury
  float p = bmp.readPressure(); //pascals
  
  dataString += String(c, 2);
  dataString += ",";
  dataString += String(f, 2);
  dataString += ",";
  dataString += String(p, 2);
  dataString += ",";
  
  if ((gps.location.age() < 1000 || gps.location.isUpdated()) && gps.location.isValid()) {
    if (gps.satellites.isValid() && (gps.satellites.value() > 3)) {
      dataString += (gps.course.isValid() ? (int)gps.course.deg() : 0);
      dataString += ",";
      dataString += (gps.speed.isValid() ? (int)gps.speed.knots() : 0);
      dataString += ",";
      dataString += (gps.location.isValid() ? (long)gps.altitude.feet() : 0);
      dataString += ",";
      dataString += (gps.hdop.isValid() ? (int)gps.hdop.value() : 0);
      dataString += ",";
      dataString += (gps.satellites.isValid() ? (int)gps.satellites.value() : 0);
      dataString += ",";
      dataString += (gps.location.isValid() ? (int)gps.location.age() : 0);
    
      float lat = gps.location.isValid() ? gps.location.lat() : 0;
      float lng = gps.location.isValid() ? gps.location.lng() : 0;
      
      dataString += ",";
      dataString += String(lat, 6);
      dataString += ",";
      dataString += String(lng, 6);
      dataString += ",";
      dataString += gps.charsProcessed();
      dataString += ",";
      dataString += gps.failedChecksum();
      dataString += ",";

      if (gps.date.isValid())
      {
        if (gps.date.month() < 10) dataString += String(F("0"));
        dataString += String(gps.date.month());
        dataString += String(F("/"));
        if (gps.date.day() < 10) dataString += String(F("0"));
        dataString += String(gps.date.day());
        dataString += String(F("/"));
        if (gps.date.year() < 10) dataString += String(F("0"));
        dataString += String(gps.date.year());
      }
      else
        dataString += "00/00/00";

      dataString += String(F(","));
  
      if (gps.time.isValid())
      {
        if (gps.time.hour() < 10) dataString += String(F("0"));
        dataString += String(gps.time.hour());
        dataString += String(F(":"));
        if (gps.time.minute() < 10) dataString += String(F("0"));
        dataString += String(gps.time.minute());
        dataString += String(F(":"));
        if (gps.time.second() < 10) dataString += String(F("0"));
        dataString += String(gps.time.second());
        dataString += String(F("."));
        dataString += String(gps.time.centisecond());
      }

      gpsready = true;
    }
  }

  if (gpsready || bypassGPS) {
    // open the file. note that only one file can be open at a time,
    // so you have to close this one before opening another.
    //File dataFile = SD.open("datalog.txt", FILE_WRITE);
  
    // if the file is available, write to it:
    // if (dataFile) {
    //   dataFile.println(dataString);
    //   //dataFile.close();
    //   dataFile.flush();

    // }
    // if the file isn't open, pop up an error:
    // else {
    //   Serial.println("error opening datalog.txt");
    // }
    // print to the serial port too:
    Serial.println(dataString);
  }

  delay(2000);
}

void initGPS(){
  Serial.print("\ninitializing gps...");
  
  serialgps.begin(GPSBaud);
  delay(2000);
  if (!serialgps.available()) {
    Serial.println("GPS initialization failed");
    while (1);
  }
  else {
    resetGPS();
    setGPS_DynamicMode6();

    Serial.println("GPS initialized");
  }
}

void initBMP(){
  Serial.print("\ninitializing bmp180...");

  unsigned status;
  
  status = bmp.begin();
  if (!status) {
    Serial.println("failed");
  }
  else {
    Serial.println("bmp initialized");
  }
}

void sendUBX(uint8_t *MSG, uint8_t len) {
  serialgps.flush();
  serialgps.write(0xFF);
  wait(100);
  for(int i=0; i<len; i++) {
    serialgps.write(MSG[i]);
  }
}

boolean getUBX_ACK(uint8_t *MSG) {
  uint8_t b;
  uint8_t ackByteID = 0;
  uint8_t ackPacket[10];
  unsigned long startTime = millis();

  // Construct the expected ACK packet    
  ackPacket[0] = 0xB5;	// header
  ackPacket[1] = 0x62;	// header
  ackPacket[2] = 0x05;	// class
  ackPacket[3] = 0x01;	// id
  ackPacket[4] = 0x02;	// length
  ackPacket[5] = 0x00;
  ackPacket[6] = MSG[2];	// ACK class
  ackPacket[7] = MSG[3];	// ACK id
  ackPacket[8] = 0;		// CK_A
  ackPacket[9] = 0;		// CK_B

  // Calculate the checksums
  for (uint8_t ubxi=2; ubxi<8; ubxi++) {
    ackPacket[8] = ackPacket[8] + ackPacket[ubxi];
    ackPacket[9] = ackPacket[9] + ackPacket[8];
  }

  while (1) {

    // Test for success
    if (ackByteID > 9) {
      // All packets in order!
      return true;
    }

    // Timeout if no valid response in 3 seconds
    if (millis() - startTime > 3000) { 
      return false;
    }

    // Make sure data is available to read
    if (serialgps.available()) {
      b = serialgps.read();

      // Check that bytes arrive in sequence as per expected ACK packet
      if (b == ackPacket[ackByteID]) { 
        ackByteID++;
      } 
      else {
        ackByteID = 0;	// Reset and look again, invalid order
      }

    }
  }
}

void resetGPS() {
  uint8_t set_reset[] = {
    0xB5, 0x62, 0x06, 0x04, 0x04, 0x00, 0xFF, 0x87, 0x00, 0x00, 0x94, 0xF5           };
  sendUBX(set_reset, sizeof(set_reset)/sizeof(uint8_t));
}

void setGPS_DynamicMode6()
{
  int gps_set_sucess = 0;
  uint8_t setdm6[] = {
    0xB5, 0x62, 0x06, 0x24, 0x24, 0x00, 0xFF, 0xFF, 0x06,
    0x03, 0x00, 0x00, 0x00, 0x00, 0x10, 0x27, 0x00, 0x00,
    0x05, 0x00, 0xFA, 0x00, 0xFA, 0x00, 0x64, 0x00, 0x2C,
    0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x16, 0xDC
  };

  while (!gps_set_sucess)
  {
    sendUBX(setdm6, sizeof(setdm6) / sizeof(uint8_t));
    gps_set_sucess = getUBX_ACK(setdm6);
  }
}

void wait(unsigned long delaytime) // Arduino Delay doesn't get CPU Speeds below 8Mhz
{
  unsigned long _delaytime=millis();
  while((_delaytime+delaytime)>=millis()){
  }
}

