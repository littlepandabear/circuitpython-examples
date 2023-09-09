import time
import array
import math
import audioio
import board
import digitalio

button = digitalio.DigitalInOut(board.A1)
button.switch_to_input(pull=digitalio.Pull.UP)

tone_volume = 0.1  # Increase this to increase the volume of the tone.
frequency = 440  # Set this to the Hz of the tone you want to generate.
length = 8000 // frequency
sine_wave = int((1 + math.sin(math.pi * 2 * 5 / length)) * tone_volume * (2 ** 15 - 1))

audio = audioio.AudioOut(board.A0,'')
sine_wave_sample = audioio.RawSample(sine_wave)

while True:
    if not button.value:
        audio.play(sine_wave_sample, loop=True)
        time.sleep(1)
        audio.stop()