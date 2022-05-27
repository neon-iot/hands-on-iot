from machine import Pin

verde = Pin(15, Pin.OUT)
amarillo = Pin(2, Pin.OUT)
rojo = Pin(0, Pin.OUT)

boton = Pin(33, Pin.IN, Pin.PULL_UP)

ultimo_estado_boton = boton.value()
c = 0

while True:
    estado_boton = boton.value()
    
    if not estado_boton and estado_boton != ultimo_estado_boton:
        c += 1
        c %= 4
        
    if c == 0:
        rojo.on()
        amarillo.off()
        verde.off()
    elif c == 1:
        rojo.on()
        amarillo.on()
        verde.off()
    elif c == 2:
        rojo.off()
        amarillo.off()
        verde.on()
    elif c == 3:
        rojo.off()
        amarillo.on()
        verde.off()
    
    ultimo_estado_boton = estado_boton