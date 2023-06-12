# NEON - Network of Competence On Internet Of Things education material
# Co-founded by the Erasmus+ Programme of the European Union
# https://www.project-neon.eu/

from time import sleep
from ulora import LoRa, SPIConfig

def on_recv(payload):
    print("From:", payload.header_from)
    print("Received:", payload.message)
    print("RSSI: {}; SNR: {}".format(payload.rssi, payload.snr))

SPIBUS = SPIConfig.esp32_2
CS = 5
RST = 4
INT = 16
FREQ = 915.0
TX_POW = 20
DIR = 0x1

lora = LoRa(SPIBUS, INT, DIR, CS, reset_pin=RST, freq=FREQ, tx_power=TX_POW, acks=True)

lora.on_recv = on_recv
lora.set_mode_rx()

while True:
    sleep(0.1)