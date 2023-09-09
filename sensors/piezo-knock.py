"""CircuitPython Basics Analog Input example"""
import time
import board
import analogio
from simpleio import map_range

# sensor setup
sensor = analogio.AnalogIn(board.A1)
threshold = 6000

while True:
    # print(sensor.value)
    mapped = map_range(sensor.value, 0, 65535, 0, 100)
    # print(mapped)

    if (sensor.value >= threshold):
        print("knocked")
    time.sleep(0.10)
