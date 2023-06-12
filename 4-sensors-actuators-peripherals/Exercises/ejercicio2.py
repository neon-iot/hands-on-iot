# NEON - Network of Competence On Internet Of Things education material
# Co-founded by the Erasmus+ Programme of the European Union
# https://www.project-neon.eu/

from machine import Pin, PWM, ADC
from time import sleep_ms

led = PWM(Pin(0), freq=1000)
adc = ADC(Pin(35), atten=ADC.ATTN_11DB)

d = 0

while True:
    d = int(adc.read() / 4095 * 1023)
    led.duty(d)

    sleep_ms(10)

