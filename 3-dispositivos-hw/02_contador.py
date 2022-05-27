from machine import Pin
from time import ticks_us

boton_inc = Pin(33, Pin.IN, Pin.PULL_UP)
boton_dec = Pin(26, Pin.IN, Pin.PULL_UP)

ultimo_estado_inc = boton_inc.value()
ultimo_estado_dec = boton_dec.value()

contador = 0

while True:
    estado_actual_inc = boton_inc.value()
    estado_actual_dec = boton_dec.value()
    
    if not estado_actual_inc and estado_actual_inc != ultimo_estado_inc:
        contador += 1
        print(contador)
    
    if not estado_actual_dec and estado_actual_dec != ultimo_estado_dec:
        contador -= 1
        print(contador)
        
    ultimo_estado_inc = estado_actual_inc
    ultimo_estado_dec = estado_actual_dec