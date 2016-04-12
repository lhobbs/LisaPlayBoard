/*
  AnalogReadSerial
  Reads an analog input on pin 0, prints the result to the serial monitor.
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

 This example code is in the public domain.
 */

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  pinMode(13, OUTPUT); //1
  pinMode(12, OUTPUT); //2
  pinMode(11, OUTPUT); //3 red
  pinMode(10, OUTPUT); //3
  pinMode(9, OUTPUT); //4 red
  pinMode(8, OUTPUT); //4
  pinMode(7, OUTPUT); //red
  pinMode(6, OUTPUT); //red
}

// the loop routine runs over and over again forever:
void loop() {
  int d = 1000;
  if (Serial.available())
  {
    char inByte = Serial.read();
    Serial.write(inByte);
    switch(inByte)
    {
      case '1':
        digitalWrite(13, HIGH);
        delay(d);
        break;
      case '2':
        digitalWrite(12, HIGH);
        delay(d);
        break;
      case '3':
        digitalWrite(11, HIGH);
        digitalWrite(10, HIGH);
        delay(d);
        break;
      case '4':
        digitalWrite(9, HIGH);
        digitalWrite(8, HIGH);
        delay(d);
        break;
      case '5':
        digitalWrite(13, HIGH);
        digitalWrite(12, HIGH);
        delay(d);
        break;
      case '6':
        digitalWrite(13, HIGH);
        digitalWrite(11, HIGH);
        digitalWrite(10, HIGH);
        delay(d);
        break;
      case '7':
        digitalWrite(13, HIGH);
        digitalWrite(9, HIGH);
        digitalWrite(8, HIGH);
        delay(d);
        break;
      case '8':
        digitalWrite(12, HIGH);
        digitalWrite(11, HIGH);
        digitalWrite(10, HIGH);
        delay(d);
        break;
      case '9':
        digitalWrite(12, HIGH);
        digitalWrite(9, HIGH);
        digitalWrite(8, HIGH);
        delay(d);
        break;
      case 'd':
        digitalWrite(11, HIGH);
        digitalWrite(10, HIGH);
        digitalWrite(9, HIGH);
        digitalWrite(8, HIGH);
        delay(d);
        break;
      case 'e':
        digitalWrite(13, LOW);
        digitalWrite(12, LOW);
        digitalWrite(10, LOW);
        digitalWrite(8, LOW);
        digitalWrite(7, HIGH);
        digitalWrite(6, HIGH);
        digitalWrite(9, HIGH);
        digitalWrite(11, HIGH);
        delay(d);
        break;
      case 'l':
        d = 500;
      default:
        digitalWrite(13, LOW);
        digitalWrite(12, LOW);
        digitalWrite(11, LOW);
        digitalWrite(10, LOW);
        digitalWrite(9, LOW);
        digitalWrite(8, LOW);
        digitalWrite(7, LOW);
        digitalWrite(6, LOW);
        break;
    }
    /*if (d >= 100) {
      d = d - 100;
    }*/
  }
  
  
  // read the input on analog pin 0:
  int sensor1 = analogRead(A0);
  int sensor2 = analogRead(A1);
  int sensor3 = analogRead(A2);
  int sensor4 = analogRead(A3);
  if (sensor1 > 550) {
    digitalWrite(13, HIGH);
  }
  else {
    digitalWrite(13, LOW);
  }
  if (sensor2 > 700) {
    digitalWrite(12, HIGH);
  }
  else {
    digitalWrite(12, LOW);
  }
  if (sensor3 > 800) {
    digitalWrite(11, 128);
    digitalWrite(10, 128);
    //delay(1000);
  }
  else {
    digitalWrite(11, LOW);
    digitalWrite(10, LOW);
  }
  if (sensor4 > 700) {
    digitalWrite(9, HIGH);
    digitalWrite(8, HIGH);
  }
  else {
    digitalWrite(9, LOW);
    digitalWrite(8, LOW);
  }
  String s1 = "sensor1 ";
  String s2 = " sensor2 ";
  String s3 = " sensor3 ";
  String s4 = " sensor4 ";
  // print out the value you read:
  Serial.println(s1 + sensor1 + s2 + sensor2 + s3 + sensor3 + s4 + sensor4);
  //Serial.println(s2 + sensor2);
  delay(1000);        // delay in between reads for stability
}
