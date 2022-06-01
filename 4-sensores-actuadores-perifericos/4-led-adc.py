from time import sleep_ms

from machine import ADC, Pin

adc = ADC(Pin(35), atten=ADC.ATTN_11DB)
verde = Pin(15, Pin.OUT)
amarillo = Pin(2, Pin.OUT)
rojo = Pin(0, Pin.OUT)

while True:
    val = adc.read_uv() / 1000

    if val < 1000:
        verde.on()
        amarillo.off()
        rojo.off()
    elif val < 2000:
        verde.off()
        amarillo.on()
        rojo.off()
    else:
        verde.off()
        amarillo.off()
        rojo.on()

    sleep_ms(10)
