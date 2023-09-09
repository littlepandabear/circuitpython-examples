"""CircuitPython Basics Analog In PWM Output example"""

import board
import pulseio
from analogio import AnalogIn
import time

# pot setup
pot = AnalogIn(board.A0) #0-655335 range depend on sensor+resistor
# led setup
led = pulseio.PWMOut(board.A1)

#helper function to more easily set PWM duty cycle
def duty_cycle_value(percent):
    return int(percent * 65535) 
        
while True:
    
    led.duty_cycle = duty_cycle_value(pot.value/100) #duty_cycle needs int
    time.sleep(0.01)


"""CircuitPython Basics Photocell Analog In, PWM Output example"""

"""
import board
import pulseio
from analogio import AnalogIn
import time
from simpleio import map_range  #library has map function


# photocell setup
photocell = AnalogIn(board.A0) #0-655335 range depend on sensor+resistor
# led setup
led = pulseio.PWMOut(board.A1)

#helper function to more easily set PWM duty cycle
def duty_cycle_value(percent):
    return int(percent * 65535) 
        
while True:
    
    mapped = map_range(photocell.value, 4000, 10000, 0, 65535) #map_range returns float
    led.duty_cycle = int(mapped) #duty_cycle needs int
    time.sleep(0.01)
"""