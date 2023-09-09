char data;

int ledPin = 9;

void setup(){
  
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  
}

void loop() {
  
   if (Serial.available()) 
   { // If data is available to read,
     data = Serial.read(); // read it and store it in data
     analogWrite(ledPin, data); //write
	 
   }

}