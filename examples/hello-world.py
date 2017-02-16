#!/usr/bin/env python

import time
import signal

import scrollphathd
from scrollphathd.fonts import font5x7

print("""
Scroll pHAT HD: Hello World

Scrolls "Hello World" across the screen
in a 5x7 pixel large font.

Press Ctrl+C to exit!

""")


scrollphathd.rotate(180)

scrollphathd.write_string("Hello World! ", x=0, y=0, font=font5x7, brightness=0.5)

while True:
    scrollphathd.show()
    scrollphathd.scroll(1)
    time.sleep(0.05)

