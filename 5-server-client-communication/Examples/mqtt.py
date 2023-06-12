# NEON - Network of Competence On Internet Of Things education material
# Co-founded by the Erasmus+ Programme of the European Union
# https://neonproject.eu/

from mqtt_as import MQTTClient, config
import uasyncio

def callback(topic, payload, retained):
    print((topic, payload, retained))
    
async def conn_handler(cliente):
    await cliente.subscribe("prueba/#", qos=0)

async def main(cliente):
    await cliente.connect()
    while True:
        await uasyncio.sleep(5)
        await cliente.publish("prueba/esp32",
                              "Mensaje de prueba", retain=False, qos=0)

config["ssid"] = "Hands On IoT"
config["wifi_pw"] = "handsoniot"
config["server"] = "10.2.13.97"
config["port"] = 1884
config["subs_cb"] = callback
config["connect_coro"] = conn_handler
client = MQTTClient(config)
MQTTClient.DEBUG = True

try:
    uasyncio.run(main(client))
finally:
    client.close()
