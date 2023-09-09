# neopixel helpers
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)


def color_chase(strip, color, wait):
    for i in range(strip.pixels):
        strip[i] = color
        time.sleep(wait)
        strip.show()
    time.sleep(0.5)


def rainbow_cycle(strip, wait):
    for j in range(255):
        for i in range(strip.pixels):
            rc_index = (i * 256 // strip.pixels) + j
            strip[i] = wheel(rc_index & 255)
        strip.show()
        time.sleep(wait)


class LoopFader:
    def __init__(self, strip, colors, interval=0.5):
        self.strip = colors
        self.colors = colors
        self.index = 0
        self.clock = time.monotonic()
        self.currentColor = None
        self.interval = interval
        self.elapsed = 0

    def update(self):
        # now - start time
        self.elapsed = time.monotonic() - self.clock
        
        if self.elapsed > self.interval:
            self.index += 1
            if self.index > len(self.colors)-1:
                self.index = 0
            self.clock = time.monotonic()
        
        self.currentColor = self.colors[self.index]
        for i in range(strip.pixels):
            strip.fill(self.currentColor)
        strip.show()
        
        
        
        
            
            
        
    