# NEON - Network of Competence On Internet Of Things education material
# Co-founded by the Erasmus+ Programme of the European Union
# https://www.project-neon.eu/

from machine import WDT
from time import sleep_ms

# Guardar este archivo en ESP32 como main.py
# para que se ejecute automáticamente

wdt = WDT(timeout=8000)
a = [20, 3, 14, 91, 42]
indice = 0

while True:
    print(f"Posición: {indice}. Elemento: {a[indice]}")
    indice += 1  # Fuerzo un bug al incrementar más allá
                 # del tamaño de la lista
    
    wdt.feed()
    sleep_ms(1000)