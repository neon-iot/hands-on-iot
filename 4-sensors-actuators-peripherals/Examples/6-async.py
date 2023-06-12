# NEON - Network of Competence On Internet Of Things education material
# Co-founded by the Erasmus+ Programme of the European Union
# https://neonproject.eu/

import uasyncio

async def tarea1():
    while True:
        print("Tarea 1")
        await uasyncio.sleep_ms(2000)
        
async def tarea2():
    while True:
        print("Tarea 2")
        await uasyncio.sleep_ms(800)
        
async def main():
    uasyncio.create_task(tarea1())
    uasyncio.create_task(tarea2())
    
    while True:
        await uasyncio.sleep_ms(1000)
        
uasyncio.run(main())