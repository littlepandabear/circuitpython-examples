import os
import board
import busio
from digitalio import DigitalInOut
import neopixel

from adafruit_esp32spi import adafruit_esp32spi
import adafruit_esp32spi.adafruit_esp32spi_wifimanager as wifimanager
import adafruit_wsgi.esp32spi_wsgiserver as server

import adafruit_lsm6ds.lsm6ds33
import adafruit_bmp280

i2c = board.I2C()

# accelerometer
lsm6ds33 = adafruit_lsm6ds.lsm6ds33.LSM6DS33(i2c)
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)


# This example depends on the 'static' folder in the examples folder
# being copied to the root of the circuitpython filesystem.
# This is where our static assets like html, js, and css live.

# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

try:
    import json as json_module
except ImportError:
    import ujson as json_module

print("ESP32 SPI simple web server test!")

#  externally connected ESP32:
esp32_cs = DigitalInOut(board.D10)
esp32_ready = DigitalInOut(board.D9)
esp32_reset = DigitalInOut(board.D6)

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(
    spi, esp32_cs, esp32_ready, esp32_reset
)  # pylint: disable=line-too-long

print("MAC addr:", [hex(i) for i in esp.MAC_address])
print("MAC addr actual:", [hex(i) for i in esp.MAC_address_actual])

# Use below for Most Boards
status_light = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.2)
# If you want to connect to wifi with secrets:
wifi = wifimanager.ESPSPI_WiFiManager(esp, secrets, status_light)
wifi.connect()

# If you want to create a WIFI hotspot to connect to with secrets:
# secrets = {"ssid": "My ESP32 AP!", "password": "supersecret"}
# wifi = wifimanager.ESPSPI_WiFiManager(esp, secrets, status_light)
# wifi.create_ap()

# To you want to create an un-protected WIFI hotspot to connect to with secrets:"
# secrets = {"ssid": "My ESP32 AP!"}
# wifi = wifimanager.ESPSPI_WiFiManager(esp, secrets, status_light)
# wifi.create_ap()


class SimpleWSGIApplication:
    """
    An example of a simple WSGI Application that supports
    basic route handling and static asset file serving for common file types
    """

    INDEX = "/index.html"
    CHUNK_SIZE = 8912  # max number of bytes to read at once when reading files

    def __init__(self, static_dir=None, debug=False):
        self._debug = debug
        self._listeners = {}
        self._start_response = None
        self._static = static_dir
        if self._static:
            self._static_files = ["/" + file for file in os.listdir(self._static)]

    def __call__(self, environ, start_response):
        """
        Called whenever the server gets a request.
        The environ dict has details about the request per wsgi specification.
        Call start_response with the response status string and headers as a list of tuples.
        Return a single item list with the item being your response data string.
        """
        if self._debug:
            self._log_environ(environ)

        self._start_response = start_response
        status = ""
        headers = []
        resp_data = []

        key = self._get_listener_key(
            environ["REQUEST_METHOD"].lower(), environ["PATH_INFO"]
        )
        if key in self._listeners:
            status, headers, resp_data = self._listeners[key](environ)
        if environ["REQUEST_METHOD"].lower() == "get" and self._static:
            path = environ["PATH_INFO"]
            if path in self._static_files:
                status, headers, resp_data = self.serve_file(
                    path, directory=self._static
                )
            elif path == "/" and self.INDEX in self._static_files:
                status, headers, resp_data = self.serve_file(
                    self.INDEX, directory=self._static
                )

        self._start_response(status, headers)
        return resp_data

    def on(self, method, path, request_handler):
        """
        Register a Request Handler for a particular HTTP method and path.
        request_handler will be called whenever a matching HTTP request is received.

        request_handler should accept the following args:
            (Dict environ)
        request_handler should return a tuple in the shape of:
            (status, header_list, data_iterable)

        :param str method: the method of the HTTP request
        :param str path: the path of the HTTP request
        :param func request_handler: the function to call
        """
        self._listeners[self._get_listener_key(method, path)] = request_handler

    def serve_file(self, file_path, directory=None):
        status = "200 OK"
        headers = [("Content-Type", self._get_content_type(file_path))]

        full_path = file_path if not directory else directory + file_path

        def resp_iter():
            with open(full_path, "rb") as file:
                while True:
                    chunk = file.read(self.CHUNK_SIZE)
                    if chunk:
                        yield chunk
                    else:
                        break

        return (status, headers, resp_iter())

    def _log_environ(self, environ):  # pylint: disable=no-self-use
        print("environ map:")
        for name, value in environ.items():
            print(name, value)

    def _get_listener_key(self, method, path):  # pylint: disable=no-self-use
        return "{0}|{1}".format(method.lower(), path)

    def _get_content_type(self, file):  # pylint: disable=no-self-use
        ext = file.split(".")[-1]
        if ext in ("html", "htm"):
            return "text/html"
        if ext == "js":
            return "application/javascript"
        if ext == "css":
            return "text/css"
        if ext in ("jpg", "jpeg"):
            return "image/jpeg"
        if ext == "png":
            return "image/png"
        return "text/plain"


# Our HTTP Request handlers
def get_accel(environ):  # pylint: disable=unused-argument

    accel = {
        'x': lsm6ds33.acceleration[0],
        'y': lsm6ds33.acceleration[1],
        'z': lsm6ds33.acceleration[2]
    }
    data = json_module.dumps(accel)
    return ("200 OK", [], data)
    
def get_temp(environ):  # pylint: disable=unused-argument
    temp = "Temperature: {:.1f} C".format(bmp280.temperature)
    return ("200 OK", [], temp)


# Here we create our application, setting the static directory location
# and registering the above request_handlers for specific HTTP requests
# we want to listen and respond to.
static = "/static"
try:
    static_files = os.listdir(static)
    if "index.html" not in static_files:
        raise RuntimeError(
            """
            This example depends on an index.html, but it isn't present.
            Please add it to the {0} directory""".format(
                static
            )
        )
except (OSError) as e:
    raise RuntimeError(
        """
        This example depends on a static asset directory.
        Please create one named {0} in the root of the device filesystem.""".format(
            static
        )
    ) from e

web_app = SimpleWSGIApplication(static_dir=static)

# HTTP Requests
web_app.on("GET", "/ajax/get_accel", get_accel)

web_app.on("GET", "/ajax/get_temp", get_temp)


# Here we setup our server, passing in our web_app as the application
server.set_interface(esp)
wsgiServer = server.WSGIServer(80, application=web_app)

print("open this IP in your browser: ", esp.pretty_ip(esp.ip_address))

# Start the server
wsgiServer.start()
while True:
    # Our main loop where we have the server poll for incoming requests
    try:
        wsgiServer.update_poll()
        # Could do any other background tasks here, like reading sensors
    except (ValueError, RuntimeError) as e:
        print("Failed to update server, restarting ESP32\n", e)
        wifi.reset()
        continue
