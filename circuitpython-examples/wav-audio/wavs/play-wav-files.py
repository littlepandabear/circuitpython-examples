import board
import time
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
import audioio
import touchio
import simpleio


# Analog audio output on A0, using two audio files
# place wavs in root folder of circuitpy drive
audiofiles = ["rimshot.wav", "laugh.wav"]

# Capacitive touch on A2
touch = touchio.TouchIn(board.A2)

button = DigitalInOut(board.D4)
button.direction = Direction.INPUT
button.pull = Pull.UP

######################### HELPERS ##############################

def play_file(filename):
    print("")
    print("----------------------------------")
    print("playing file "+filename)
    f = open(filename, "rb")
    a = audioio.AudioOut(board.A0, f)
    a.play()
    while a.playing:
        pass
    print("finished")
    print("----------------------------------")

######################### LOOP ##############################

while True:

  if touch.value:
      print("A2 touched!", end ="\t")
      play_file(audiofiles[0])

  if not button.value:
      print("Button D4 pressed!", end ="\t")
      play_file(audiofiles[1])


  print("")