int triggerPin = 9;

int echoPin = 10; 

float pulse_width, distance;

void setup() {
  pinMode(triggerPin, OUTPUT);
  pinMode(echoPin, INput);
  Serial.begin(9600);
  delay(2000);
}

void loop() {
  digitalWrite(triggerPin, HIGH);
  delay(10000);
  pulse_width = PulseIn(echoPin, HIGH);
  distance = (pulse_width * 0.343)/200;
  Serial.print("Distance");
  Serial.print(distance);
  Serial.print(" m)");
  delay (500)

}
