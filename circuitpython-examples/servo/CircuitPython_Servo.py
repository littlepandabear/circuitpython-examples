"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pulseio
from adafruit_motor import servo

# create a PWMOut object on Pin D9.
# duty_cycle cycles the pin with 50% duty cycle (half of 65535)
# frequency is the the target frequency in Hertz
pwm = pulseio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
