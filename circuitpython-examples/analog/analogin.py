"""CircuitPython Basics Analog Input example"""
import time
import board
import analogio
from simpleio import map_range

# sensor setup
sensor = analogio.AnalogIn(board.A1)
threshold = 100

while True:
    print(sensor.value)
    mapped= map_range(sensor.value, 0, 65535, 0, 300)
    if (sensor.value >= threshold){
        print("knock")
    }
    time.sleep(0.10)

