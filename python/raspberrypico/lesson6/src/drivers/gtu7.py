import utime, time

class GTU7 :
    """GT-U7 driver for capturing GPS data."""
    
    def __init__(self, uart) :
        self.uart = uart
        
        self.buff = bytearray(255, 'utf-8')
        self.timeout = 8 # total length of time in seconds to poll for GPS data

        
    def gpgga(self, timeout=None) :
        """Get GPS GPGGA data

        Parameters
        ----------
        timeout : int, optional
            The total length of time in seconds to poll for GPS data

        Returns
        -------
        list
            a list of GPS GPGGA data ordered by latutide, longitude, num_sattelites, gps_time
        """
        
        if not timeout: timeout = self.timeout
        
        timeout_e = time.time() + timeout
        
        while True:
            self.buff = str(self.uart.readline())
            parts = self.buff.split(',')
            
            # Example GPGGA (http://aprs.gids.nl/nmea/#gga)
            # $GPGGA,hhmmss.ss,llll.ll,a,yyyyy.yy,a,x,xx,x.x,x.x,M,x.x,M,x.x,xxxx*hh
            if (parts[0] == "b'$GPGGA" and len(parts) == 15) :
                
                # Check if there are values in each part, otherwise continue to poll for GPS data
                if(parts[1] and parts[2] and parts[3] and parts[4] and parts[5] and parts[6] and parts[7]) :
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
                    
                    return [gps_time, float(latitude), float(longitude), int(num_satellites)]
            
            if (time.time() > timeout_e) :
                return []
            
    def gprmc(self, timeout=None) :
        """Get GPS GPRMC data

        Parameters
        ----------
        timeout : int, optional
            The total length of time in seconds to poll for GPS data

        Returns
        -------
        list
            a list of formatted GPS GPRMC data
        """
        
        if not timeout: timeout = self.timeout
        
        timeout_e = time.time() + timeout
        
        while True:
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
                
                return [gps_date, gps_time, float(latitude), float(longitude), float(parts[7])]
            
            if (time.time() > timeout_e) :
                return []
    
    
    def __convertToDegree(self, degrees) :
        firstdigits = int(degrees / 100) 
        nexttwodigits = degrees - float(firstdigits * 100) 

        converted = float(firstdigits + nexttwodigits / 60.0)
        converted = '{0:.6f}'.format(converted)
        
        return str(converted)


    def __stringifyGpsTime(self, t) :
        return t[0:2] + ":" + t[2:4] + ":" + t[4:6]
    
    
    def __stringifyGpsDate(self, d) :
        return d[0:2] + "-" + d[2:4] + "-" + d[4:6]
        

