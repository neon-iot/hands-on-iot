# NEON - Network of Competence On Internet Of Things education material
# Co-founded by the Erasmus+ Programme of the European Union
# https://neonproject.eu/

import uasyncio
from machine import Pin

delta = 500

async def boton(boton, incrementa_delta):
    global delta

    ultimo_estado = False
    while True:
        estado = not boton.value()
        if estado != ultimo_estado and estado:
            await uasyncio.sleep_ms(10)
            nuevo_estado = not boton.value()
            if nuevo_estado:
                if incrementa_delta:
                    delta += 50
                    if delta > 1000:
                        delta = 1000
                else:
                    delta -= 50
                    if delta < 50:
                        delta = 50
                print("Nuevo delta:", delta)
        ultimo_estado = estado
        await uasyncio.sleep_ms(10)
    

async def main():
    uasyncio.create_task(boton(Pin(33, Pin.IN, Pin.PULL_UP), True))
    uasyncio.create_task(boton(Pin(26, Pin.IN, Pin.PULL_UP), False))
    
    led = Pin(15, Pin.OUT)
    
    while True:
        led.on()
        await uasyncio.sleep_ms(delta)
        led.off()
        await uasyncio.sleep_ms(delta)
        
uasyncio.run(main())


