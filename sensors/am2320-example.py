import time
import board
import busio
import adafruit_am2320

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_am2320.AM2320(i2c)

while True:
    # relative_humidity: 0-100%
    print("Humidity: {0}%".format(sensor.relative_humidity))

    # temperature: degrees Celsius
    print("Temperature: {0}C".format(sensor.temperature))

    # wait 2 sec
    time.sleep(2)