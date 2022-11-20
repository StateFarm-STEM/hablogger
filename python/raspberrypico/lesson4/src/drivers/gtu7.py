import utime, time

class GTU7 :
    """GT-U7 driver for capturing GPS data."""
    
    def __init__(self, uart) :
        self.gtu7 = uart
        
        self.buff = bytearray(255)
        self.poll = 500 # polling interval in ms
        self.timeout = 8 # total length of time in seconds to poll for GPS data
        
        self.gtu7_init(uart)
        
        
    def gtu7_init(self, uart) :
        self.buff = uart.readline()

        
    def get_gps_data(self, timeout=None, poll=None) :
        """Get GPS data

        Parameters
        ----------
        timeout : int, optional
            The total length of time in seconds to poll for GPS data
        poll : int, optional
            The polling interval in ms

        Returns
        -------
        list
            a list of GPS GPGGA data ordered by latutide, longitude, num_sattelites, gps_time
        """
        
        if not timeout: timeout = self.timeout
        if not poll: poll = self.poll
        
        timeout_e = time.time() + timeout
        
        while True:
            self.buff = str(self.gtu7.readline())
            
            parts = self.buff.split(',')
            
            # Example 15 length GPGGA data. Sometimes this varies. We are only interested in the integrity of length 15.
            # 15 ["b'$GPGGA", '161636.00', '4026.77522', 'N', '08902.07820', 'W', '2', '11', '0.79', '262.3', 'M', '-33.2', 'M', '', "0000*67\\r\\n'"]
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
                    gps_time = parts[1][0:2] + ":" + parts[1][2:4] + ":" + parts[1][4:6]
                    
                    return [float(latitude), float(longitude), int(num_satellites), gps_time]
            
            if (time.time() > timeout_e) :
                return None
            
            utime.sleep_ms(self.poll)
            
    def __convertToDegree(degrees) :
        firstdigits = int(degrees / 100) 
        nexttwodigits = degrees - float(firstdigits * 100) 

        converted = float(firstdigits + nexttwodigits / 60.0)
        converted = '{0:.6f}'.format(converted)
        
        return str(converted)
