import serial
import time
import datetime

portname = '/dev/cu.usbmodem1412401' 
serialport = serial.Serial(port=portname,baudrate=115200,timeout=0.5)

while True:
	incoming = serialport.readline().strip()
	
	data = incoming.decode('utf-8')
	if data != "":
		values = data.split(';')
		print("received: {0}".format(values))
		
		ts = datetime.datetime.now()
		
		f = open("datalog.txt", "a")
		f.write("temp C: {}, temp F: {}, timestamp: {} \n".format(values[0], values[1], ts))
		f.close()
	time.sleep(1)