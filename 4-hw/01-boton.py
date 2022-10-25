from machine import Pin

led = Pin(0, Pin.OUT)
boton = Pin(33, Pin.IN, Pin.PULL_UP)

while True:
     if not boton.value():  # activo bajo
         led.on()
     else:
         led.off()
