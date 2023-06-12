# NEON - Network of Competence On Internet Of Things education material
# Co-founded by the Erasmus+ Programme of the European Union
# https://neonproject.eu/

from time import sleep
from ulora import LoRa, SPIConfig

SPIBUS = SPIConfig.esp32_2
CS = 5
RST = 4
INT = 16
FREQ = 915.0
TX_POW = 20
DIR = 0x2
DIR_DEST = 0x1

lora = LoRa(SPIBUS, INT, DIR, CS, reset_pin=RST, freq=FREQ, tx_power=TX_POW, acks=True)

n = 0
while True:
    n += 1
    if lora.send_to_wait(f"Mensaje de prueba {n}", DIR_DEST):
        print("Mensaje enviado")
    else:
        print("Falló transmisión del mensaje")

    sleep(2)