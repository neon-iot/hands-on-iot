# NEON - Network of Competence On Internet Of Things education material
# Co-founded by the Erasmus+ Programme of the European Union
# https://www.project-neon.eu/

from machine import Pin, ADC
from time import sleep_ms

adc = ADC(Pin(35), atten=ADC.ATTN_11DB)

while True:
    print(f"{adc.read_uv()} uV ({adc.read()})")
    sleep_ms(100)