"""CircuitPython Basics Digital Out example"""
import time
import board
import digitalio
import time

# LED setup.
led = digitalio.DigitalInOut(board.A1)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
