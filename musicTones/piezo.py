import time
import board
import random
from adafruit_circuitplayground.express import cpx
 

while True:
    if cpx.switch:
        for x in range(10):
            cpx.pixels[x] = (255,0,200)
    else:
        for x in range(10):
            cpx.pixels[x] = (0,0,0)
        #time.sleep(1)            
    if cpx.button_b:
    #time.sleep(3)
        print("button")
        cpx.start_tone(590)
    elif cpx.button_a:
        print('other button')
        cpx.start_tone(2000)
        for x in range(10):
            cpx.pixels[x] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            time.sleep(.05)
    else:
        cpx.stop_tone()

