import serial
import time

portname = '/dev/cu.usbmodem1412401' 
serialport = serial.Serial(port=portname,baudrate=115200,timeout=0.5)

while True:
	serialport.write(b'hello!')
	time.sleep(2)