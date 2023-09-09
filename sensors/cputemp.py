import microcontroller

while True:
    print("CPU Temp: ", microcontroller.cpu.temperature)
    print("C to F: ", microcontroller.cpu.temperature * (9/5) + 32 )