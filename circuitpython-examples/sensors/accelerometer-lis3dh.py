import board
import adafruit_lis3dh

# Uncomment _one_ of the hardware setups below depending on your wiring:

# Hardware I2C setup:
import busio
i2c = busio.I2C(board.SCL, board.SDA)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c)

# Set range of accelerometer (can be RANGE_2_G, RANGE_4_G, RANGE_8_G or RANGE_16_G).
lis3dh.range = adafruit_lis3dh.RANGE_2_G


# set_tap(1 or 2 for num taps, threshold val)
lis3dh.set_tap(2, 60)


# Loop forever printing accelerometer values
while True:
    
    # Read accelerometer values (in m / s ^ 2).  Returns a 3-tuple of x, y,
    # z axis values.
    x, y, z = lis3dh.acceleration
    print(x, y, z)
    
    # Divide accelerometer values by 9.806 (standard gravity) to convert to Gs.
    x, y, z = [
        value / adafruit_lis3dh.STANDARD_GRAVITY for value in lis3dh.acceleration
    ]
    print("x = %0.3f G, y = %0.3f G, z = %0.3f G" % (x, y, z))
    
    
    # shake event
    if lis3dh.shake(shake_threshold=15):
        print("Shaken!")
        
    # tap event
    if lis3dh.tapped:
        print("Tapped!")    
    
    # Small delay to keep things responsive but give time for interrupt processing.
    time.sleep(0.1)