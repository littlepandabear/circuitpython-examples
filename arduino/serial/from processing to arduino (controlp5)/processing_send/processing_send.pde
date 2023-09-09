import processing.serial.*;

Serial port;//Create object from Serial class

int data; // Data received from the serial port

//control p5 library
import controlP5.*;
ControlP5 cp5;

void setup() {
  
  size(displayWidth, displayHeight);

  println(Serial.list());

  String portName = Serial.list()[3];
  port = new Serial(this, portName, 9600);
  //port = new Serial(this, "/dev/tty.usbmodem1411", 9600); //same as above

  cp5 = new ControlP5(this);
  
  cp5.addSlider("slider")
     .setRange(0,255)
     .setValue(128)
     .setPosition(100,160)
     .setSize(500,100);  
  
}

void draw() { 
  
  float sliderValue = cp5.getController("slider").getValue();
  data = int(sliderValue);
  port.write(data); 
  
}