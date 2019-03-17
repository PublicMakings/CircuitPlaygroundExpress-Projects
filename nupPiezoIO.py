# reads the analog voltage level from a 10k potentiometer
# connected to GND, 3.3V, and pin A1
# and prints the results to the REPL
import time
import array
import math
import audioio
import board
import digitalio
from analogio import AnalogOut

#440 1590 2090
FREQUENCY = 2090  # 440 Hz middle 'A'
SAMPLERATE = 8000  # 8000 samples/second, recommended!
 
# Generate one period of sine wav.
length = SAMPLERATE // FREQUENCY
sine_wave = array.array("H", [0] * length)
for i in range(length):
    sine_wave[i] = int(math.sin(math.pi * 2 * i / 18) * (2 ** 15) + 2 ** 15)
 
# enable the speaker
speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.direction = digitalio.Direction.OUTPUT
speaker_enable.value = True
 
audio = audioio.AudioOut(board.A0)
sine_wave_sample = audioio.RawSample(sine_wave)

#analogin = AnalogIn(board.A1)
analog_out = AnalogOut(board.A0)

#while True:

#    if cpx.button_b: 
#        audio.play(sine_wave_sample, loop=True)  # keep playing the sample o$
#        time.sleep(3)  # until...
#        audio.stop()  # we te

#def getVoltage(pin):  # helper
 #   return (pin.value * 3.3) / 65536


while True:
    time.sleep(3)
 #   print("Analog Voltage: %f" % getVoltage(analogin))
    
 #   audio.play(sine_wave_sample, loop=True)  # keep playing the sample over a$
    time.sleep(.5)  # until...
  #  audio.stop()  # we t 
    for i in range(0, 65535, 64):
        analog_out.value = i
 
 
#while True:
 #   print("Analog Voltage: %f" % getVoltage(analogin))
  #  time.sleep(0.1)
