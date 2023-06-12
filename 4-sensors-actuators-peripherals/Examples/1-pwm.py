# NEON - Network of Competence On Internet Of Things education material
# Co-founded by the Erasmus+ Programme of the European Union
# https://neonproject.eu/

from machine import Pin, PWM
from time import sleep_ms

led = PWM(Pin(0), freq=1000)

d = 0

while True:
    led.duty(d)
    d += 10
    if d > 1023:
        d = 0
    sleep_ms(10)