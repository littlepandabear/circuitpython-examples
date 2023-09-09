"""CircuitPython Basics Analog In Out example"""
import board
import analogio
import time

#potentiometer setup
pot = analogio.AnalogIn(board.A1)

# led setup
led = analogio.AnalogOut(board.A0)

#convert analog in signal to 0-3.3 voltage
def get_voltage(pin):
    return (pin.value * 3.3) / 65536


#convert digital signal to analog out
def dac_value(volts):
    return int(volts / 3.3 * 65535)


while True:
    
    #get pot voltage
    pot_volts = get_voltage(pot);
    
    #get value from voltage and set as led value
    led.value = dac_value(pot_volts)

    #delay between reading
    time.sleep(0.1)
    
    
"""
while True:
    led.value = pot.value

    #delay between reading
    time.sleep(0.1)
"""
