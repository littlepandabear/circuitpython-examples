import time
import board
import analogio
from simpleio import map_range

# sensor setup
sensor = analogio.AnalogIn(board.A1)

# 40cm
threshold = 40

# helper
def get_voltage(pin):
    return (pin.value * 3.3) / 65536

while True:
    # raw value
    print(sensor.value)
    
    # convert to voltage
    voltage = get_voltage(sensor.value)
   
    # map voltage to CM
    cm = map_range(voltage, 0.4, 2.3, 10, 80)
    
    # check cm against threshold to trigger
    if (cm < threshold){
        print("triggered")
    } 
    
    # delay between readings
    time.sleep(0.10)

