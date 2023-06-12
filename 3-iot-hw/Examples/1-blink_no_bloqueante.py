# NEON - Network of Competence On Internet Of Things education material
# Co-founded by the Erasmus+ Programme of the European Union
# https://neonproject.eu/

from time import sleep_ms, ticks_ms
from machine import Pin

led = Pin(15, Pin.OUT)

ultimo_parpadeo = 0

while True:
    if ticks_ms() - ultimo_parpadeo > 1000:
        if led.value() == 0:
            led.on()
        else:
            led.off()
        ultimo_parpadeo = ticks_ms()
