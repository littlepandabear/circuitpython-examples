import time
import board
import microcontroller

while True:

    # temperature:  Celsius 
    c = microcontroller.cpu.temperature
    
    # temperature: Fareinheit
    f = microcontroller.cpu.temperature*(9/5)+32
    
    # output
    print(c, ";", f)

    # wait 2 sec
    time.sleep(2)