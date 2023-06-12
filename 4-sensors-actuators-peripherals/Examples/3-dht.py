# NEON - Network of Competence On Internet Of Things education material
# Co-founded by the Erasmus+ Programme of the European Union
# https://neonproject.eu/

from dht import DHT11
from machine import Pin
from time import sleep_ms

dht = DHT11(Pin(32))

while True:
    try:
        dht.measure()
        print(f"Temperatura: {dht.temperature()} °C")
        print(f"Humedad: {dht.humidity()} %")
    except OSError:
        print("Error al leer la medición")
        
    sleep_ms(1000)
