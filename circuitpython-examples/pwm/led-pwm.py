"""CircuitPython Basics Analog Output PWM example"""
import board
import pulseio
import time

# led setup
led = pulseio.PWMOut(board.A2)

# helper function to more easily set PWM duty cycle
def duty_cycle_value(percent):
    return int(percent * 65535) 
        
while True:
    for i in range(100):
        led.duty_cycle = duty_cycle_value(i / 100) 
        time.sleep(0.01)
    # reverse direction - range(start,stop,step)
    for i in range(100, -1, -1):
        led.duty_cycle = duty_cycle_value(i / 100) 
        time.sleep(0.01)
    
"""
#helper function to more easily set PWM duty cycle
def duty_cycle_value(percent):
    return int(percent * 65535) 
        
led.duty_cycle = duty_cycle_value(0.5) 

led.duty_cycle = duty_cycle_value(i / 100)         
"""
