# NEON - Network of Competence On Internet Of Things education material
# Co-founded by the Erasmus+ Programme of the European Union
# https://neonproject.eu/

from machine import Pin
from time import sleep_ms

led = Pin(0, Pin.OUT)

while True:
    led.on()
    sleep_ms(500)
    led.off()
    sleep_ms(500)