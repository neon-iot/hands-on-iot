from time import sleep_ms

from machine import ADC, PWM, Pin

pwm = PWM(Pin(0), freq=10000)
adc = ADC(Pin(35), atten=ADC.ATTN_11DB)

escala = 1024 / 2**12

while True:
    val = adc.read()
    pwm.duty(int(val * escala))
    sleep_ms(10)
