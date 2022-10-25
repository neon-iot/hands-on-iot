from machine import Pin
from time import sleep_ms, ticks_ms

ultimo_estado_boton_rapido = False
ultimo_estado_boton_lento = False

boton_rapido = Pin(33, Pin.IN, Pin.PULL_UP)
boton_lento = Pin(26, Pin.IN, Pin.PULL_UP)
led = Pin(15, Pin.OUT)

delta = 1000
ultimo_parpadeo = ticks_ms()

while True:
    estado_boton_rapido = boton_rapido.value()
    if estado_boton_rapido != ultimo_estado_boton_rapido and estado_boton_rapido == False:
        sleep_ms(10)
        if boton_rapido.value() == False:
            delta -= 50
            if delta < 50:
                delta = 50
            print("Nuevo delta:", delta)
    
    estado_boton_lento = boton_lento.value()
    if estado_boton_lento != ultimo_estado_boton_lento and estado_boton_lento == False:
        sleep_ms(10)
        if boton_lento.value() == False:
            delta += 50  
            if delta > 5000:
                delta = 5000
            print("Nuevo delta:", delta)
                
    if ticks_ms() - ultimo_parpadeo > delta:
        ultimo_parpadeo = ticks_ms()
        led.value(not led.value())
    
    ultimo_estado_boton_rapido = estado_boton_rapido
    ultimo_estado_boton_lento = estado_boton_lento
