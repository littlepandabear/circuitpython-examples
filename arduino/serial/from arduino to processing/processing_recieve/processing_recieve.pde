import processing.serial.*;

Serial port; //Create object from Serial class

String data; // Data received from the serial port


void setup() {
  
  println(Serial.list());

  String portName = Serial.list()[3];
  port = new Serial(this, portName, 9600);
  //port = new Serial(this, "/dev/tty.usbmodem1411", 9600); //same as above

  size(displayWidth, displayHeight);
  
}

void draw() { 

  if (port.available() > 0) {  // If data is available
	 
    String incoming = port.readStringUntil('\n'); // read it and store it in val
	
	if (incoming != null){
		data = incoming;
	}
  }
  
  println(data); //print it out in the console
  
  //display text
  text(data, displayWidth/2, displayHeight/2)

  
}