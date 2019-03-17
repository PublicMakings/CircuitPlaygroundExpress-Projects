    # CircuitPlaygroundExpress_NeoPixel
     
    import time
     
    import board
    import neopixel
     
    pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
    pixels.fill((255, 255, 0))
    pixels.show()

