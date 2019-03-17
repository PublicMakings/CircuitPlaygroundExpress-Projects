import audioio
import board
import digitalio
import array
import time
import math
import touchio
from adafruit_circuitplayground.express import cpx
#import neopixel 

touch1 = touchio.TouchIn(board.A1)
touch2 = touchio.TouchIn(board.A2)
touch3 = touchio.TouchIn(board.A3)
touch4 = touchio.TouchIn(board.A4)
touch5 = touchio.TouchIn(board.A5)
touch6 = touchio.TouchIn(board.A6)
touch7 = touchio.TouchIn(board.A7)

#bright= 0.2
#pixels=neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=bright)
#pixels.fill((0,0,0))
#pixels.show()

length = 8000 // 205
sine_wave = array.array("H", [0] * length)
for i in range(length):
    sine_wave[i] = int(math.sin(math.pi * 2 * i / 18) * (2 ** 15) + 2 ** 15)
sine_wave = audioio.RawSample(sine_wave)
 
#spkrenable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
#spkrenable.direction = digitalio.Direction.OUTPUT
#spkrenable.value = True



cpx.detect_taps = 1


while True: 
    # Prep a buffer to record into
    #if cpx_button_b:
    #    b = bytearray(200)
    #    with audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA, sample_rate=16000) as mic:
    #        mic.record(b, len(b))
    
    if cpx.button_a:
 #       pixels.fill((140,30,240))
 #       pixels.show()
        
        # Generate one period of sine wav.
        
        print("whoop")
        dac = audioio.AudioOut(board.SPEAKER)
        dac.play(sine_wave, loop=True)
        time.sleep(1)
        dac.stop()
        dac.deinit() 
        print("whawp") 
  #      pixels.fill((0,0,0))
  #      pixels.show()


###another interesting feature

    if cpx.switch:
        cpx.pixels.brightness = .2
        cpx.pixels[0] = (220,0,255)        
        print("living the dream")
        time.sleep(.1)
        cpx.pixels[0] = (0,0,0)
    
    if cpx.tapped:
        print("Single tap detected!")

    if cpx.shake(10):
       print("Shake detected!")
    time.sleep(.001) 
    if cpx.shake():
        print("Shakey Shake detected!")
    time.sleep(.001)
    
    

#while True:
    if touch1.value:
        print("A1 touched!")
    if touch2.value:
        print("A2 touched!")
    if touch3.value:
        print("A3 touched!")
    if touch4.value:
        print("A4 touched!")
    if touch5.value:
        print("A5 touched!")
    if touch6.value:
        print("A6 touched!")
    if touch7.value:
        print("A7 touched!")
 
    time.sleep(0.01)

