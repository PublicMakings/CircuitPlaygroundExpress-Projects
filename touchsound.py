""" soundTouch.py  
    
    circuitPython // Circuit Playground Express 
    - buttons trigger sound & light
    - can record audio with sparkle lights
    - can playback audio with lights
"""
#setup the board
import audiobusio, audioio
import board, digitalio, neopixel, touchio
from adafruit_circuitplayground.express import cpx

import time, random

#setup buttons and pixels
touch1 = touchio.TouchIn(board.A1)
touch2 = touchio.TouchIn(board.A2)
touch3 = touchio.TouchIn(board.A3)
touch4 = touchio.TouchIn(board.A4)
touch5 = touchio.TouchIn(board.A5)
touch6 = touchio.TouchIn(board.A6)
touch7 = touchio.TouchIn(board.A7)

buttons = [touch1, touch2, touch3, touch4, touch5, touch6, touch7]

pixelBrightness = 0.4
pixels = neopixel.Neopixel(board.NEOPIXEL, 10, brightness=pixelBrightness)


def record():
    '''record 8-bit unsigned sample from PDMin CPython api'''

    # Prep a buffer to record into
    b = bytearray(200)
    with audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA) as mic:
        audio = mic.record(b, len(b))
    return audio

def glowPlay():
'''Main loop gets x, y and z axis acceleration, 
   prints the values, and turns on
   red, green and blue, at levels related to the x, y and z values.'''

    if cpx.switch:
        print("Slide switch off!")
        cpx.pixels.fill((random(120), random(50), 200))
        continue
    else:
        R = 0
        G = 0
        B = 0
        x, y, z = cpx.acceleration
        print((x, y, z))
        if x:
            R = R + abs(int(x))
        if y:
            G = G + abs(int(y))
        if z:
            B = B + abs(int(z))
        cpx.pixels.fill((R, G, B))


if __name__ == "__main__":
    
    for buttton in buttons:
        if buttton.value:
            pixels.fill((random(255),random(255),random(255)))
            pixels.show()
            time.sleep(1)
            pixels.fill((0,0,0))
            pixels.show()
