from time import sleep_ms

from dht import DHT11
from machine import Pin

verde = Pin(15, Pin.OUT)
rojo = Pin(0, Pin.OUT)

dht = DHT11(Pin(32))

while True:
    dht.measure()
    t = dht.temperature()

    print(t)
    if t < 30:
        verde.on()
        rojo.off()
    else:
        verde.off()
        rojo.on()

    sleep_ms(1000)
