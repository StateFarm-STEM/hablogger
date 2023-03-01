import utime, time, math

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
            a list of GPS GPGGA data ordered by [gps_time, latitude, longitude, num_satellites]
        """
        
        if not timeout: timeout = self.timeout
        
        timeout_e = time.time() + timeout
        
        while True:
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
            
    def gprmc(self, timeout=None) :
        """Get GPS GPRMC data

        Parameters
        ----------
        timeout : int, optional
            The total length of time in seconds to poll for GPS data

        Returns
        -------
        list
            a list of formatted GPS GPRMC data ordered by [gps_date, gps_time, latitude, longitude, speed]
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