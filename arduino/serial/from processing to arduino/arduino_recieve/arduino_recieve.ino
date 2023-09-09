char data;

int ledPin = 13;

void setup(){
  
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  
}

void loop() {
  
   if (Serial.available()) 
   { // If data is available to read,
     data = Serial.read(); // read it and store it in val
   }
   if (data == '1') 
   { // If 1 was received
     digitalWrite(ledPin, HIGH); // turn the LED on
   } else {
     digitalWrite(ledPin, LOW); // otherwise turn it off
   }
   delay(10); // Wait 10 milliseconds for next reading
}
  

