Code Explanation

TinyGPS++ is used to handle the GPS data, extracting latitude and longitude.

The panic button is checked in the loop, and when pressed, the location data is sent via the SIM800C module as an SMS alert.

The sendSMS() function is responsible for formatting the GPS coordinates and sending them via GSM.
