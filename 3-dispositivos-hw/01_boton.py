from machine import Pin

boton = Pin(33, Pin.IN, Pin.PULL_UP)
led = Pin(0, Pin.OUT)

while True:
    estado = not boton.value()
    led.value(estado)