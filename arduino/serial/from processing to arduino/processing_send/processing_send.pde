import processing.serial.*;

Serial port;//Create object from Serial class

String data; // Data received from the serial port


void setup() {
  
  println(Serial.list());

  String portName = Serial.list()[3];
  port = new Serial(this, portName, 9600);
  //port = new Serial(this, "/dev/tty.usbmodem1411", 9600); //same as above

  size(displayWidth, displayHeight);
  
  
}

void draw() { 

  if (mousePressed == true) 
  { //if we clicked in the window
   port.write('1');  //send a 1  
  } else 
  { //otherwise
  port.write('0');  //send a 0
  }   
  
}