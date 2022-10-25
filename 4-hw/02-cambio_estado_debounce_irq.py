from machine import Pin, disable_irq, enable_irq
from time import sleep_ms

def irq_boton(pin):
    s = disable_irq()
    sleep_ms(10)
    if pin.value() == False:
        global pulsado
        pulsado = not pulsado
        led_verde.value(pulsado)
        led_rojo.value(not pulsado)
    enable_irq(s)

led_verde = Pin(15, Pin.OUT)
led_rojo = Pin(0, Pin.OUT)
boton = Pin(33, Pin.IN, Pin.PULL_UP)

pulsado = False
boton.irq(handler=irq_boton, trigger=Pin.IRQ_FALLING)
