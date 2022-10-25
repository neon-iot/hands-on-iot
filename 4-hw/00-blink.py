from machine import Pin
from time import sleep_ms

led = Pin(0, Pin.OUT)
while True:
    led.on()
    sleep_ms(500)
    led.off()
    sleep_ms(500)