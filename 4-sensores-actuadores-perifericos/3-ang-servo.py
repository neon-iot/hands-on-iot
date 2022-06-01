from time import sleep_ms

from machine import ADC, PWM, Pin

servo = PWM(Pin(14), freq=50)
adc = ADC(Pin(35), atten=ADC.ATTN_11DB)
min_val = 51
max_val = 102
escala = (max_val - min_val) / 2**12

while True:
    val = adc.read()

    servo.duty(int(val * escala + min_val))
    sleep_ms(10)
