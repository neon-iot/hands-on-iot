# NEON - Network of Competence On Internet Of Things education material
# Co-founded by the Erasmus+ Programme of the European Union
# https://neonproject.eu/

import network

wlan = network.WLAN(network.STA_IF)
if not wlan.active():
   wlan.active(True)

redes = wlan.scan()
for red in redes:
    print(f"{red[0]}. Canal {red[2]}. RSSI: {red[3]}")