from time import sleep_ms

import network
from umqtt.robust import MQTTClient

wlan = network.WLAN(network.STA_IF)
if not wlan.active():
    wlan.active(True)

if not wlan.isconnected():
    wlan.connect("LPMS", "truchard")

    print("Conectando...")
    while not wlan.isconnected():
        sleep_ms(1000)

config = wlan.ifconfig()
print(f"Conectado con ip {config[0]}")


def callback(topic, msg):
    topic = topic.decode()
    msg = msg.decode()

    if topic == "/servidor":
        print(f"Llegó {msg} de {topic}")


cliente = MQTTClient("nombre", "mqtt.fi.mdp.edu.ar", keepalive=30)
print("Conectando a servidor MQTT...")
cliente.set_callback(callback)
cliente.connect(clean_session=False)
print("Conectado")
cliente.subscribe("/servidor")

while True:
    cliente.publish("/alumnos/yo", "hola")
    cliente.check_msg()
    sleep_ms(500)

cliente.disconnect()
