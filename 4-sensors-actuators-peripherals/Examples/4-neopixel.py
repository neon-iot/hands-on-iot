# NEON - Network of Competence On Internet Of Things education material
# Co-founded by the Erasmus+ Programme of the European Union
# https://www.project-neon.eu/

from neopixel import NeoPixel
from machine import Pin
from time import sleep_ms
from random import randint

np = NeoPixel(Pin(27), 3)

while True:
    c1 = randint(0, 255)
    c2 = randint(0, 255)
    c3 = randint(0, 255)
        
    np[0] = (c1, c2, c3)
    np[1] = (c2, c3, c1)
    np[2] = (c3, c2, c1)
    np.write()
    
    sleep_ms(1000)