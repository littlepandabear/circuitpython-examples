import time
import board
import adafruit_tcs34725

i2c = board.I2C()

sensor = adafruit_tcs34725.TCS34725(i2c)

# properties you can both read and write to change how the sensor behaves
# integration time of the sensor in milliseconds.  Must be a value between 2.4 and 614.4 ms
sensor.integration_time = 150
#  gain of the sensor, must be a value of 1, 4, 16, 60
sensor.gain = 4


# Main loop reading color and printing it every second.
while True:
    # Raw data from the sensor in a 4-tuple of red, green, blue, clear light component values
    print(sensor.color_raw)
    
    # color_rgb_bytes - A 3-tuple of the red, green, blue color values.  These are returned as bytes from 0 to 255 (0 is low intensity, 255 is maximum intensity).

    color = sensor.color
    color_rgb = sensor.color_rgb_bytes
    print(
        "RGB color as 8 bits per channel int: #{0:02X} or as 3-tuple: {1}".format(
            color, color_rgb
        )
    )

    # Read the color temperature and lux of the sensor too.
    
    # color_temperature - The color temperature in Kelvin detected by the sensor.  This is computed from the color and might not be super accurate!
    # lux - The light intensity in lux detected by the sensor.  This is computed from the color and might not be super accurate!
    
    temp = sensor.color_temperature
    lux = sensor.lux
    print("Temperature: {0}K Lux: {1}\n".format(temp, lux))
    
    # Delay for a second and repeat.
    time.sleep(1.0)