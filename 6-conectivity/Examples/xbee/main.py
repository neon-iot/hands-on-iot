# NEON - Network of Competence On Internet Of Things education material
# Co-founded by the Erasmus+ Programme of the European Union
# https://neonproject.eu/

from machine import UART
from time import sleep_ms

uart = UART(2, baudrate=9600)
n = 0

while True:
    n += 1
    if uart.any() > 0:
        buf = uart.read()
        print(buf.decode())
        
    uart.write(f"Mensaje de prueba {n}")
    sleep_ms(1000)