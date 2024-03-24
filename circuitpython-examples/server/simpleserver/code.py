# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import busio
from digitalio import DigitalInOut
import neopixel

from adafruit_esp32spi import adafruit_esp32spi
import adafruit_esp32spi.adafruit_esp32spi_wifimanager as wifimanager
import adafruit_wsgi.esp32spi_wsgiserver as server
from adafruit_wsgi.wsgi_app import WSGIApp


i2c = board.I2C()

# import sensor
import adafruit_bmp280
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
temp = ""

# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

# This example depends on a WSGI Server to run.
# We are using the wsgi server made for the ESP32

print("ESP32 SPI simple web app test!")
# If you have an externally connected ESP32:
esp32_cs = DigitalInOut(board.D10)
esp32_ready = DigitalInOut(board.D9)
esp32_reset = DigitalInOut(board.D6)

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(
    spi, esp32_cs, esp32_ready, esp32_reset
)  # pylint: disable=line-too-long

"""Use below for Most Boards"""
status_light = neopixel.NeoPixel(
    board.NEOPIXEL, 1, brightness=0.2
)  # Uncomment for Most Boards
"""Uncomment below for ItsyBitsy M4"""
# import adafruit_dotstar as dotstar
# status_light = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=1)

## If you want to connect to wifi with secrets:
wifi = wifimanager.ESPSPI_WiFiManager(esp, secrets, status_light, debug=True)
wifi.connect()

## If you want to create a WIFI hotspot to connect to with secrets:
# secrets = {"ssid": "My ESP32 AP!", "password": "supersecret"}
# wifi = wifimanager.ESPSPI_WiFiManager(esp, secrets, status_light)
# wifi.create_ap()

## To you want to create an un-protected WIFI hotspot to connect to with secrets:"
# secrets = {"ssid": "My ESP32 AP!"}
# wifi = wifimanager.ESPSPI_WiFiManager(esp, secrets, status_light)
# wifi.create_ap()

# Here we create our application, registering the
# following functions to be called on specific HTTP GET requests routes

web_app = WSGIApp()


@web_app.route("/")
def home(request):  # pylint: disable=unused-argument
    return ("200 OK", [], temp)

@web_app.route("/led_on/<r>/<g>/<b>")
def led_on(request, r, g, b):  # pylint: disable=unused-argument
    print("led on!")
    status_light.fill((int(r), int(g), int(b)))
    return ("200 OK", [], "led on!")


@web_app.route("/led_off")
def led_off(request):  # pylint: disable=unused-argument
    print("led off!")
    status_light.fill(0)
    return ("200 OK", [], "led off!")


# Here we setup our server, passing in our web_app as the application
server.set_interface(esp)
wsgiServer = server.WSGIServer(80, application=web_app)

print("open this IP in your browser: ", esp.pretty_ip(esp.ip_address))

# print(esp.get_time())
# Start the server
wsgiServer.start()
while True:
    # Our main loop where we have the server poll for incoming requests
    try:
        wsgiServer.update_poll()
        # Could do any other background tasks here, like reading sensors
        temp = "Temperature: {:.1f} C".format(bmp280.temperature)
        
    except (ValueError, RuntimeError) as e:
        print("Failed to update server, restarting ESP32\n", e)
        wifi.reset()
        continue