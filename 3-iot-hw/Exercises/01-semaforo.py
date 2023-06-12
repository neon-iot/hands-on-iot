# NEON - Network of Competence On Internet Of Things education material
# Co-founded by the Erasmus+ Programme of the European Union
# https://neonproject.eu/

from machine import Pin
from time import sleep_ms

led_verde = Pin(15, Pin.OUT)
led_rojo = Pin(0, Pin.OUT)
led_amarillo = Pin(2, Pin.OUT)
boton = Pin(33, Pin.IN, Pin.PULL_UP)

posicion = 0
POSICIONES = ((1, 0, 0), (1, 1, 0), (0, 0, 1), (0, 1, 0))

ultimo_estado = False

while True:
    estado = not boton.value()
    
    if estado != ultimo_estado:
        sleep_ms(50)
        nuevo_estado = not boton.value()
        if nuevo_estado:
            posicion += 1
            posicion %= 4
            led_rojo.value(POSICIONES[posicion][0])
            led_amarillo.value(POSICIONES[posicion][1])
            led_verde.value(POSICIONES[posicion][2])

    ultimo_estado = estado
