#touch demo

import board
import touchio

# Capacitive touch on A2
touch = touchio.TouchIn(board.A2)

while True:

  if touch.value:
      print("A2 touched!")