from machine import Pin

led_verde = Pin(15, Pin.OUT)
led_rojo = Pin(0, Pin.OUT)
boton = Pin(33, Pin.IN, Pin.PULL_UP)

estado = False
ultimo_estado_boton = False

while True:
    estado_boton = not boton.value()
    
    if estado_boton != ultimo_estado_boton and estado_boton:
        estado = not estado
        
        led_verde.value(pulsado)
        led_rojo.value(not pulsado)
    
    ultimo_estado_boton = estado_boton
