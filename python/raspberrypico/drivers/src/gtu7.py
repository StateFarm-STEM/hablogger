import utime, time, random

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
            if (parts[0] == "b'$GPGGA" and len(parts) == 15) :
                try:
                    latitude = self.__convertToDegree(parts[2])
                except:
                    latitude = parts[2]

                if (parts[3] == 'S'):
                    latitude = '-' + latitude

                try:
                    longitude = self.__convertToDegree(parts[4])
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
    
    
    def __convertToDegree(self, degrees) :
        firstdigits = int(degrees / 100) 
        nexttwodigits = degrees - float(firstdigits * 100) 

        converted = float(firstdigits + nexttwodigits / 60.0)
        converted = '{0:.6f}'.format(converted)
        
        return str(converted)


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
