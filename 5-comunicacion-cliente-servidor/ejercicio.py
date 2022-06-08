from time import ticks_ms

import network
from umqtt.robust import MQTTClient

from machine import Pin, PWM, ADC
from neopixel import NeoPixel

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

led_verde = Pin(15, Pin.OUT)
led_amarillo = Pin(2, Pin.OUT)
led_rojo = Pin(0, Pin.OUT)
boton = Pin(33, Pin.IN, Pin.PULL_UP)
servo = PWM(Pin(14), freq=50)
adc = ADC(Pin(35), atten=ADC.ATTN_11DB)
np = NeoPixel(Pin(27), 1)

estado_boton = False
ultimo_estado_boton = boton.value()

min_val = 51
max_val = 102
escala = (max_val - min_val) / 180

def callback(topic, msg):
    topic = topic.decode()
    msg = msg.decode()

    if topic == "/alumnos/yo/led_verde":
        led_verde.value(msg == "1")
    elif topic == "/alumnos/yo/led_amarillo":
        led_amarillo.value(msg == "1")
    elif topic == "/alumnos/yo/led_rojo":
        led_rojo.value(msg == "1")
    elif topic == "/alumnos/yo/servo":
        ang = int(msg)
        if ang < 0:
            ang = 0
        elif ang > 180:
            ang = 180
        servo.duty(int(ang * escala + min_val))
    elif topic == "/alumnos/yo/neopixel":
        colores = msg.split(",")
        if len(colores) != 3:
            return
        r = int(colores[0])
        g = int(colores[1])
        b = int(colores[2])
        
        np[0] = (b, r, g)
        np.write()        


cliente = MQTTClient("nombre", "mqtt.fi.mdp.edu.ar", keepalive=30)
print("Conectando a servidor MQTT...")
cliente.set_callback(callback)
cliente.connect(clean_session=False)
print("Conectado")
cliente.subscribe("/alumnos/yo/#")

ultima_actualizacion = ticks_ms()

while True:
    if ticks_ms() - ultima_actualizacion > 1000:
        cliente.check_msg()
        ultima_actualizacion = ticks_ms()
    
    estado_boton = not boton.value()
    if estado_boton != ultimo_estado_boton:
        if estado_boton:
            cliente.publish("/servidor/yo", str(adc.read_uv()))
    
    ultimo_estado_boton = estado_boton

cliente.disconnect()
