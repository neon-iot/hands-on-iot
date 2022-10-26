from machine import Pin, disable_irq, enable_irq
from time import sleep_ms

led_verde = Pin(15, Pin.OUT)
led_rojo = Pin(0, Pin.OUT)
led_amarillo = Pin(2, Pin.OUT)
boton = Pin(33, Pin.IN, Pin.PULL_UP)

estado = 0
ESTADOS = ((1, 0, 0), (1, 1, 0), (0, 0, 1), (0, 1, 0))

def irq_boton(pin):
    s = disable_irq()
    sleep_ms(10)
    if pin.value() == False:
        global estado
        estado += 1
        estado %= len(ESTADOS)
    enable_irq(s)

boton.irq(handler=irq_boton, trigger=Pin.IRQ_FALLING)

delta = 0

while True:                
    led_rojo.value(ESTADOS[estado][0])
    led_amarillo.value(ESTADOS[estado][1])
    led_verde.value(ESTADOS[estado][2])

    sleep_ms(20)
