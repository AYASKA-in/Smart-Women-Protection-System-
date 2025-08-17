
#include <SoftwareSerial.h> #include <TinyGPS++.h>
SoftwareSerial gpsSerial(10, 11);	// GPS module (Neo-6M) connected to pins 10 (RX) and 11 (TX)
SoftwareSerial sim800c(8, 9);	// SIM800C module connected to pins 8 (RX) and 9 (TX)

TinyGPSPlus gps;
float latitude, longitude;
const int buttonPin = 7;	// Button connected to pin 7 bool buttonPressed = false;
void setup() {
gpsSerial.begin(9600);		// Start GPS module at 9600 baud sim800c.begin(9600);			// Start SIM800C module at 9600 baud Serial.begin(9600);	// Serial monitor for debugging
pinMode(buttonPin, INPUT_PULLUP);	// Configure button with internal pull-up resistor
delay(2000);	// Allow modules to initialize
Serial.println("System ready. Press the button to send SMS alert with location (if available).");
configureGSM();	// Set GSM module to 2G mode
}
void loop() {
// Check if the button is pressed
if (digitalRead(buttonPin) == LOW) { // Button pressed (active low) buttonPressed = true;
delay(200);	// Debounce delay
}

if (buttonPressed) {
Serial.println("Button pressed! Gathering GPS location (if available) and sending SMS alert...");
gatherAndSendSMS();
buttonPressed = false;	// Reset button press flag
}
}
void configureGSM() {
// Set the SIM800C module to 2G mode
sim800c.println("AT+CNMP=13");	// Set network mode to 2G (GSM only) delay(1000);
while (sim800c.available()) {
Serial.println(sim800c.readString()); // Print any response from GSM
}
Serial.println("GSM configured to 2G mode.");
}
void gatherAndSendSMS() { bool gpsDataAvailable = false;
// Attempt to get valid GPS coordinates unsigned long startTime = millis();
while (millis() - startTime < 5000) { // Try for up to 5 seconds while (gpsSerial.available()) {
int data = gpsSerial.read();
if (gps.encode(data) && gps.location.isValid()) { latitude = gps.location.lat();
longitude = gps.location.lng();
// Print GPS coordinates to Serial Monitor Serial.print("Latitude: ");

Serial.println(latitude, 6);	// Print with 6 decimal places Serial.print("Longitude: ");
Serial.println(longitude, 6); gpsDataAvailable = true; break;
}
}
if (gpsDataAvailable) break;
}

sendSMS(gpsDataAvailable);	// Send SMS, with or without GPS data
}
void sendSMS(bool gpsDataAvailable) { String message = "Help! ";
if (gpsDataAvailable) {
message += "My location is:\n";
message += "Latitude: " + String(latitude, 6) + ", "; message += "Longitude: " + String(longitude, 6);
} else {
message += "Unable to retrieve GPS location.";
}
sim800c.println("AT+CMGF=1");	// Set SMS mode to text delay(1000);
// Send SMS to the first phone number sim800c.println("AT+CMGS=\"+917013377185\""); // Replace with your number, include country code
delay(1000);
sim800c.print(message);		// Write the message content sim800c.write(26);	// ASCII code for Ctrl+Z to send the message delay(3000);
// Send SMS to the second phone number sim800c.println("AT+CMGS=\"+919121881060\"");	// Second number, include country code
delay(1000);
sim800c.print(message);		// Write the message content sim800c.write(26);	// ASCII code for Ctrl+Z to send the message delay(3000);
Serial.println("Alert message sent to both numbers!");
}
