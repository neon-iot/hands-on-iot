from time import sleep_ms

from machine import PWM, Pin

pwm = PWM(Pin(0), freq=10000)
c = 0

while True:
    if c < 1024:
        pwm.duty(c)
    else:
        pwm.duty(2047 - c)

    c += 10
    c %= 2048
    sleep_ms(10)
