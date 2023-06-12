# NEON - Network of Competence On Internet Of Things education material
# Co-founded by the Erasmus+ Programme of the European Union
# https://neonproject.eu/

from machine import Pin
from time import sleep_ms

boton_subir = Pin(26, Pin.IN, Pin.PULL_UP)
boton_bajar = Pin(33, Pin.IN, Pin.PULL_UP)

ultimo_estado_subir = False
ultimo_estado_bajar = False

contador = 0

while True:
    estado_subir = not boton_subir.value()
    estado_bajar = not boton_bajar.value()
    
    if estado_subir != ultimo_estado_subir:
        sleep_ms(50)
        nuevo_estado = not boton_subir.value()
        if nuevo_estado:
            contador += 1
            print(f"Pulsado {contador} veces")
            
    if estado_bajar != ultimo_estado_bajar:
        sleep_ms(50)
        nuevo_estado = not boton_bajar.value()
        if nuevo_estado:
            contador -= 1
            print(f"Pulsado {contador} veces")
    
    ultimo_estado_subir = estado_subir
    ultimo_estado_bajar = estado_bajar