Circuit Diagram and Connections:

SIM800C GSM Module:

The SIM800C is used for sending SMS alerts. It communicates with the Arduino using SoftwareSerial.

 SIM800C TX (Transmit) → Pin 9 (Arduino RX)
 SIM800C RX (Receive) → Pin 8 (Arduino TX)
 SIM800C VCC → 5V (from Arduino or an external 3.7-4.2V battery if required by the module)
 SIM800C GND → Ground (GND) Neo-6M GPS Module:
The Neo-6M GPS module tracks the GPS location, sending the coordinates to the Arduino.

 GPS TX (Transmit) → Pin 11 (Arduino RX)
 GPS RX (Receive) → Pin 10 (Arduino TX)
 GPS VCC → 5V (from Arduino)
 GPS GND → Ground (GND) Panic Button:
A simple push button is used to trigger the SMS alert when pressed.

 One terminal of the button → Pin 7 (Arduino)
 Other terminal → Ground (GND)

Power Supply:

You can use the 5V pin from the Arduino to power the GPS module and the SIM800C module if its voltage regulator supports 5V. If the SIM800C module requires a 3.7-4.2V power supply, use an external battery for powering it.

Breadboard Layout:

1.Place the Arduino on the breadboard or next to the breadboard.
2.Connect the SIM800C module:

oTX (SIM800C) → Pin 9 (Arduino)
oRX (SIM800C) → Pin 8 (Arduino)
oVCC (SIM800C) → 5V or external power
oGND (SIM800C) → GND
3.Connect the Neo-6M GPS module:

oTX (GPS) → Pin 11 (Arduino)
oRX (GPS) → Pin 10 (Arduino)
oVCC (GPS) → 5V
oGND (GPS) → GND
4.Panic Button:

oOne side of the button → Pin 7 (Arduino)
oOther side of the button → GND
5.Power Supply:

oArduino Uno can be powered via USB or an external power supply.
oIf needed, power the SIM800C separately using a 3.7-4.2V battery.
