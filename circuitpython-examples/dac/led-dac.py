"""CircuitPython Basics Analog Output (dac) example"""
import board
import analogio

# led setup
led = analogio.AnalogOut(board.A0)

"""
#convert digital signal to analog out
def dac_value(volts):
    return int(volts / 3.3 * 65535)
    
led.value = dac_value(2.5)
"""

while True:
    # Count up from 0 to 65535, with 64 increment
    # which ends up corresponding to the DAC's 10-bit range
    for i in range(0, 65535, 64):
        led.value = i
        

    
