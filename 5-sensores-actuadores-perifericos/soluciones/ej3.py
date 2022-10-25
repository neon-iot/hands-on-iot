from machine import Pin, PWM, ADC
from time import sleep_ms

servo = PWM(Pin(14), freq=50) 
adc = ADC(Pin(35), atten=ADC.ATTN_11DB)

escala = (120 - 20) / (2 ** 12)

while True:
    lectura = adc.read()
    servo.duty(round(25 + escala * lectura))
    sleep_ms(10)