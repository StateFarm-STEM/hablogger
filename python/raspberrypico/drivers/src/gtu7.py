import utime, time, math, random

class GTU7 :
    """GT-U7 driver for capturing GPS data."""
    
    def __init__(self, uart) :
        self.uart = uart
        
        self.buff = bytearray(255, 'utf-8')
        self.timeout = 8 # total length of time in seconds to poll for GPS data

        
    def gpgga(self, timeout=None, fake=False) :
        """Get GPS GPGGA data

        Parameters
        ----------
        timeout : int, optional
            The total length of time in seconds to poll for GPS data
        fake : boolean, optional
            Return fake data. Useful if GPS signal is not available

        Returns
        -------
        list
            a list of GPS GPGGA data ordered by [gps_time, latitude, longitude, num_satellites]
        """
        
        if not timeout: timeout = self.timeout
        
        timeout_e = time.time() + timeout
        
        while True:
            if fake :
                return [self.__stringifyFakeTime(utime.localtime(time.time())),
                        4026.774,
                        -8902.08,
                        random.randint(6,9)]
            
            self.buff = str(self.uart.readline())
            parts = self.buff.split(',')
            
            # Example GPGGA (http://aprs.gids.nl/nmea/#gga)
            # $GPGGA,hhmmss.ss,llll.ll,a,yyyyy.yy,a,x,xx,x.x,x.x,M,x.x,M,x.x,xxxx*hh
            # https://latlongdata.com/lat-long-converter/
            if (parts[0] == "b'$GPGGA" and len(parts) == 15) :
                #print(parts)
                try:
                    #latitude = self.__convertToDegree(parts[2])
                    latitude = parts[2]
                except:
                    latitude = parts[2]

                if (parts[3] == 'S'):
                    latitude = '-' + latitude

                try:
                    #longitude = self.__convertToDegree(parts[4])
                    longitude = parts[4]
                except:
                    longitude = parts[4]

                if (parts[5] == 'W') :
                    longitude = '-' + longitude

                num_satellites = parts[7]
                gps_time = self.__stringifyGpsTime(parts[1])
                
                return [gps_time,
                        float(latitude) if latitude else '',
                        float(longitude) if longitude else '',
                        int(num_satellites) if num_satellites else '']
            
            if (time.time() > timeout_e) :
                return []
            
    def gprmc(self, timeout=None, fake=False) :
        """Get GPS GPRMC data

        Parameters
        ----------
        timeout : int, optional
            The total length of time in seconds to poll for GPS data
        fake : boolean, optional
            Return fake data. Useful if GPS signal is not available

        Returns
        -------
        list
            a list of formatted GPS GPRMC data ordered by [gps_date, gps_time, latitude, longitude, speed]
        """
        
        if not timeout: timeout = self.timeout
        
        timeout_e = time.time() + timeout
        
        while True:
            if fake :
                return [self.__stringifyFakeDate(utime.localtime(time.time())),
                        self.__stringifyFakeTime(utime.localtime(time.time())),
                        4026.774,
                        -8902.08,
                        round(random.uniform(0.0,0.1),3)]
            
            self.buff = str(self.uart.readline())
            parts = self.buff.split(',')
            
            
            # Example GPRMC (http://aprs.gids.nl/nmea/#rmc)
            # $GPRMC,hhmmss.ss,A,llll.ll,a,yyyyy.yy,a,x.x,x.x,ddmmyy,x.x,a*hh
            if (parts[0] == "b'$GPRMC" and len(parts) == 13) :

                try:
                    latitude = self.__convertToDegree(parts[3])
                except:
                    latitude = parts[3]

                if (parts[4] == 'S'):
                    latitude = '-' + latitude

                try:
                    longitude = self.__convertToDegree(parts[5])
                except:
                    longitude = parts[5]

                if (parts[6] == 'W') :
                    longitude = '-' + longitude

                gps_time = self.__stringifyGpsTime(parts[1])
                
                gps_date = self.__stringifyGpsDate(parts[9])
            
                return [gps_date,
                        gps_time,
                        float(latitude) if latitude else '',
                        float(longitude) if longitude else '',
                        float(parts[7]) if parts[7] else '']
            
            if (time.time() > timeout_e) :
                return []
    
    
    def __convertToDegree(self, ddm) :
        degrees = math.floor(ddm / 100)
        minutes = ddm - degrees * 100
        dd = degrees + minutes / 60.0
        dd = '{0:.6f}'.format(dd)
        
        return str(dd)


    def __stringifyGpsTime(self, t) :
        if t :
            return t[0:2] + ":" + t[2:4] + ":" + t[4:6]
        else :
            return ''
    
    
    def __stringifyGpsDate(self, d) :
        if d :
            return d[0:2] + "-" + d[2:4] + "-" + d[4:6]
        else :
            return ''
        
    def __stringifyFakeTime(self, t) :
        if t :
            return str(t[3]) + ":" + str(t[4]) + ":" + str(t[5])
        else :
            return ''

    def __stringifyFakeDate(self, d) :
        if d :
            return str(d[1]) + ":" + str(d[2]) + ":" + str(d[0])
        else :
            return ''

    def sendUBX(self, msg):
        self.uart.flush()
        self.uart.write(bytes([0xFF]))
        time.sleep_ms(100)
        #for c in msg:
        #print(str(type(msg)))
        self.uart.write(msg)
                      
    def getUBX_ACK(self, msg): 
        startTime = time.ticks_ms()
        ackByteId = 0
        
        # Construct the expected ACK packet    
        ackPacket = bytearray([0xB5, 0x62, 0x05, 0x01, 0x02, 0x00, msg[2], msg[3], 0x00, 0x00])
      
        # Calculate the checksums THIS IS NOT CALCULATING RIGHT
        for u in range (2, 8):
            ackPacket[8] = ackPacket[8] + ackPacket[u]
            ackPacket[9] = ackPacket[9] + ackPacket[8]
       
        while True:
            # Test for success
            if ackByteId > 9:
                # All bytes in order!
                return True
            
            # Timeout if no valid response in 3 seconds
            if time.ticks_diff(startTime, time.ticks_ms()) > 3000:
                return false
            
            # Make sure data is available to read
            if self.uart.any():
                b = self.uart.read(1)
                
                # Check that bytes arrive in sequence as per expected ACK packet
                if b[0] == ackPacket[ackByteId]:
                    ackByteId = ackByteId + 1
                else:
                    # Reset and look again, invalid order
                    ackByteId = 0
        
    def resetGPS(self):
        set_reset = bytes([0xB5, 0x62, 0x06, 0x04, 0x04, 0x00, 0xFF, 0x87, 0x00, 0x00, 0x94, 0xF5])
        self.sendUBX(set_reset)

    def setGPS_DynamicMode6(self):
        set_dm6 = bytes([0xB5, 0x62, 0x06, 0x24, 0x24, 0x00, 0xFF, 0xFF, 0x06,
            0x03, 0x00, 0x00, 0x00, 0x00, 0x10, 0x27, 0x00, 0x00,
            0x05, 0x00, 0xFA, 0x00, 0xFA, 0x00, 0x64, 0x00, 0x2C,
            0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x16, 0xDC])
        gps_set_success = False
        
        while not gps_set_success:
            self.sendUBX(set_dm6)
            gps_set_success = self.getUBX_ACK(set_dm6)
