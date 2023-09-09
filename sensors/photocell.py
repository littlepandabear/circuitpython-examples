"""CircuitPython Basics Analog Input example"""
"""
import board
import analogio

# photocell setup
photocell = analogio.AnalogIn(board.A0)

def adc_to_voltage(val):
    #3.3 is the outut voltge for Metro M0 pins
    return val / 65535 * 3.3

while True:
    print(photocell.value)
    print(adc_to_voltage(photocell.value))
    
"""


"""CircuitPython Basics Analog In PWM Output example"""

import board
import pulseio
from analogio import AnalogIn
import time
from simpleio import map_range  # ext library has map function

# photocell setup
photocell = AnalogIn(board.A0) # 0-655335 range depend on sensor+resistor
# led setup
led = pulseio.PWMOut(board.D6) # pwm out
        
while True:
    mapped = map_range(photocell.value, 4000, 10000, 0, 65535) # map_range returns float
    led.duty_cycle = int(mapped) # duty_cycle needs int
    time.sleep(0.01)

