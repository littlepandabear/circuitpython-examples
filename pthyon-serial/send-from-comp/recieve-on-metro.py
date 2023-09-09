import supervisor
import time

# listening
while True:
    if supervisor.runtime.serial_bytes_available:
        value = input().strip()
		# sometimes value is empty
        if value == "":
            value = None
        print("{}".format(value))
		time.sleep(2)