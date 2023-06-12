# NEON - Network of Competence On Internet Of Things education material
# Co-founded by the Erasmus+ Programme of the European Union
# https://www.project-neon.eu/

from machine import Pin, PWM
from time import sleep_ms

led = PWM(Pin(0), freq=1000)

d = 0
signo = 1

while True:
    led.duty(d)
    d += 10 * signo
    if d > 1023:
        d = 1023
        signo = -1
    elif d < 0:
        d = 0
        signo = 1
    sleep_ms(10)
