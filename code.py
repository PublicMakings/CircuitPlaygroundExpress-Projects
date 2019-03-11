'''rename that circuitpython drive
https://learn.adafruit.com/welcome-to-circuitpython/the-circuitpy-drive
'''


import board
import neopixel
import audiobusio
import audioio
import digitalio
import time

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT


def setup():
#setup pixels
    pixelBrightness = 0.05
    pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness= pixelBrightness) #determine beightness (Value can be between 0 and 1)

#setup recording
    recordLength = 5
    SAMPLERATE = 8000
    NUM_SAMPLES = 160

##setup  speaker
    spkrenable = DigitialInOut(bouard.SPEAKER_ENABLE)
    spkrenable.direction = Direction.OUTPUT
    spkrenable.value = True
    
#setup recording
    mic = audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA,
                      sample_rate=16000, bit_depth=16)

    samples = array.array('H', [0] * NUM_SAMPLES)

#debounce time
    debounceTime = 0.2

    buttonD = DigitalInOut(board.BUTTON_A) #button a is the down button
    buttonD.direction = Direction.INPUT
    buttonD.pull = Pull.DOWN
    
    buttonU = DigitalInOut(board.BUTTON_B) # button b is the up button
    buttonU.direction = Direction.INPUT
    buttonU.pull = Pull.DOWN

def normalized_rms(values):
    minbuf = int(mean(values))
    return math.sqrt(sum(float((sample - minbuf) * (sample - minbuf)) for sample in values) / len(values))

def mean(values):
    return (sum(values) / len(values))

def main():
#We begin regcording samples from the board's mic
    mic.record(samples, len(samples))
    magnitude = normalized_rms(samples)  
    print("mag = ", magnitude) #print the magnitude of the input blowing so we can track values in the serial console
    
    
    #If statements to know when up or down buttons are pushed
    #We will use a counter to track which pitch is selected
    
    if buttonU.value == True:  # If Up button is pushed then move up a pitch
        pixels.fill((0, 0, 0)) #turn all neopixels off
        counter += 1 #increase the counter by 1
        time.sleep(debounceTime) #to ensure button isn't triggered multiple times in one press we must "debounce" the button by creating a short delay after pressing it
    elif buttonD.value == True: #Do the same for the down button
        pixels.fill((0, 0, 0)) # If Down button is pushed then move down a pitch
        counter -= 1 #decrease counter by one
        time.sleep(debounceTime) #debounce button
        

 #If statement to trigger pitch when user blows into mic
    #We will say that on a any loud sound the pitch is triggered
    
    if magnitude > blowThresshold: #any time we get a sound with a magnitude greater than the value of blowThresshold, trigger the current pitch (can be changed at top where it is defined)
        length = SAMPLERATE // FREQUENCY #create length of sample
        sine_wave = array.array("H", [0] * length) #create an array for a sine wave
        for i in range(length):
            sine_wave[i] = int(math.sin(math.pi * 2 * i / 18) * (2 ** 15) + 2 ** 15) #fill the array with values
                
    #If statements for determine which pitch the board is on
    #We will use the current counter value to set which frequency, neopixel, and color should be selected


   #audio = audioio.AudioOut(board.SPEAKER)
        #sine_wave_sample = audioio.RawSample(sine_wave)
        #audio.play(sine_wave_sample, loop=True)  # Play the sample
        #time.sleep(pitchLength)  # Play for length of pitchLength
        #audio.stop()  # we tell the board to stop
        #audio.deinit()

    pixels.show() #show the desired neopixel light up on board 


if __name__ == "__main__":
    setup()
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)

