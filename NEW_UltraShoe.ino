#include <NewPing.h>

#define MAX_DIST 200

// Define the pins for the ultrasonic sensors
const int sensor1TrigPin = 22;
const int sensor1EchoPin = 22;
const int sensor2TrigPin = 23;
const int sensor2EchoPin = 23;
const int sensor3TrigPin = 12;
const int sensor3EchoPin = 12;
const int sensor4TrigPin = 13;
const int sensor4EchoPin = 13;


// Create NewPing objects for each sensor
NewPing sensor1(sensor1TrigPin, sensor1EchoPin, MAX_DIST);
NewPing sensor2(sensor2TrigPin, sensor2EchoPin, MAX_DIST);
NewPing sensor3(sensor3TrigPin, sensor3EchoPin, MAX_DIST);
NewPing sensor4(sensor4TrigPin, sensor4EchoPin, MAX_DIST);

void setup() {
  Serial.begin(9600);
}

void loop() {

  if(Serial.read()=='n') {
  // Read distances from all four sensors
  unsigned long distance1 = sensor1.ping_cm();
  unsigned long distance2 = sensor2.ping_cm();
  unsigned long distance3 = sensor3.ping_cm();
  unsigned long distance4 = sensor4.ping_cm();

  // Store the distances in a string

 String distanceString = String(distance1) + "," +
                         String(distance2) + "," +
                         String(distance3) + "," +
                         String(distance4);  

  // Display the string on the Serial Monitor
 
  Serial.print(distanceString);
  

  // Add a delay to control the loop frequency
  delay(500); // Adjust as needed

  }
}
