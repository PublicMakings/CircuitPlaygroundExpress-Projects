import audioio
import board
import digitalio
import neopixel
import touchio
import time

# setup the capacitive touch
touch1 = touchio.TouchIn(board.A1)
touch2 = touchio.TouchIn(board.A2)
touch3 = touchio.TouchIn(board.A3)
touch4 = touchio.TouchIn(board.A4)
touch5 = touchio.TouchIn(board.A5)
touch6 = touchio.TouchIn(board.A6)
touch7 = touchio.TouchIn(board.A7)

# setup neopixels
pixelBrightness =  0.5
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=pixelBrightness)
pixels.fill((0,0,0))
pixels.show()

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 85:
        return (int(pos * 3), int(255 - (pos * 3)), 0)
    elif pos < 170:
        pos -= 85
        return (int(255 - (pos * 3)), 0, int(pos * 3))
    else:
        pos -= 170
        return (0, int(pos * 3), int(255 - pos * 3))



def rainbow_cycle(wait):
    for j in range(10):
        for i in range(len(pixels)):
            idx = int((i * 256 / len(pixels)) + j * 10)
            pixels[i] = wheel(idx & 255)
        pixels.show()
        time.sleep(wait)

def simpleCircle(wait):
    RED = 0x100000  # (0x10, 0, 0) also works
    YELLOW = (0x10, 0x10, 0)
    GREEN = (0, 0x10, 0)
    AQUA = (0, 0x10, 0x10)
    BLUE = (0, 0, 0x10)
    PURPLE = (0x10, 0, 0x10)
    BLACK = (0, 0, 0)

    for i in range(len(pixels)):
        pixels[i] = RED
        time.sleep(wait)
    time.sleep(1)

    for i in range(len(pixels)):
        pixels[i] = YELLOW
        time.sleep(wait)
    time.sleep(1)

    for i in range(len(pixels)):
        pixels[i] = GREEN
        time.sleep(wait)
    time.sleep(1)

    for i in range(len(pixels)):
        pixels[i] = AQUA
        time.sleep(wait)
    time.sleep(1)

    for i in range(len(pixels)):
        pixels[i] = BLUE
        time.sleep(wait)
    time.sleep(1)

    for i in range(len(pixels)):
        pixels[i] = PURPLE
        time.sleep(wait)
    time.sleep(1)

    for i in range(len(pixels)):
        pixels[i] = BLACK
        time.sleep(wait)
    time.sleep(1)


# enable the speaker
spkrenable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = digitalio.Direction.OUTPUT
spkrenable.value = True

# make the 2 input buttons
buttonA = digitalio.DigitalInOut(board.BUTTON_A)
buttonA.direction = digitalio.Direction.INPUT
buttonA.pull = digitalio.Pull.DOWN

buttonB = digitalio.DigitalInOut(board.BUTTON_B)
buttonB.direction = digitalio.Direction.INPUT
buttonB.pull = digitalio.Pull.DOWN

# The two files assigned to buttons A & B
audiofiles = ["rimshot.wav", "laugh.wav"]


def play_file(filename):
    print("Playing file: " + filename)
    wave_file = open(filename, "rb")
    with audioio.WaveFile(wave_file) as wave:
        with audioio.AudioOut(board.A0) as audio:
            audio.play(wave)
            while audio.playing:
                pass
    print("Finished")


while True:
    if buttonA.value:
        play_file(audiofiles[0])

    if buttonB.value:

        rainbow_cycle(.0001)
        print("beeeop")

    if touch1.value:
        play_file(audiofiles[0])
        pixels.fill((255,0,200))
        pixels.show()
    if touch3.value:
        play_file(audiofiles[0])
    if touch4.value:
        play_file(audiofiles[1])
    if touch5.value:
        play_file(audiofiles[1])
    if touch6.value:
        play_file(audiofiles[1])
    if touch7.value:
        play_file(audiofiles[1])
