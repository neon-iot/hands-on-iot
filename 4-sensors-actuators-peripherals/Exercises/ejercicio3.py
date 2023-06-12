# NEON - Network of Competence On Internet Of Things education material
# Co-founded by the Erasmus+ Programme of the European Union
# https://neonproject.eu/

import uasyncio
from dht import DHT11
from machine import Pin

temperatura = 0

async def sensor():
    global temperatura
    
    dht = DHT11(Pin(32))
    while True:
        try:
            dht.measure()
            temperatura = dht.temperature()
            print(f"Temperatura: {temperatura} °C")
        except OSError:
            print("Error al leer la medición")
        uasyncio.sleep_ms(5000)

async def luces():
    led_verde = Pin(15, Pin.OUT)
    led_rojo = Pin(0, Pin.OUT)
    
    while True:
        if temperatura < 30:
            led_verde.on()
            led_rojo.off()
        else:
            led_rojo.on()
            led_verde.off()
        
        uasyncio.sleep_ms(100)
        
async def main():
    uasyncio.create_task(sensor())
    uasyncio.create_task(luces())
    
    while True:
        uasyncio.sleep_ms(1000)

uasyncio.run(main())