import network

from machine import Pin, PWM, ADC, enable_irq, disable_irq
from neopixel import NeoPixel
from dht import DHT11

from umqtt.robust import MQTTClient
from time import sleep_ms, ticks_ms
from random import randint

wlan = network.WLAN(network.STA_IF)
if not wlan.active():
    wlan.active(True)
    
if not wlan.isconnected():
    wlan.connect("FIWIFI")
    print("Conectando", end="")
    while not wlan.isconnected():
        print(".", end="")
        sleep_ms(1000)
    print()
print("Conectado")

ALUMNO = "yo"

led_verde = Pin(15, Pin.OUT)
led_amarillo = Pin(2, Pin.OUT)
led_rojo = Pin(0, Pin.OUT)
servo = PWM(Pin(14), freq=50)
np = NeoPixel(Pin(27), 3)
boton_adc = Pin(33, Pin.IN, Pin.PULL_UP)
boton_adc_pulsado = False
boton_alarma = Pin(26, Pin.IN, Pin.PULL_UP)
boton_alarma_pulsado = False
adc = ADC(Pin(35), atten=ADC.ATTN_11DB)
dht = DHT11(Pin(32))

def callback_adc(pin):
    s = disable_irq()
    sleep_ms(10)
    estado = pin.value()
    if not estado:
        global boton_adc_pulsado
        boton_adc_pulsado = True
    enable_irq(s)
    

def callback_alarma(pin):
    s = disable_irq()
    sleep_ms(10)
    estado = pin.value()
    if not estado:
        global boton_alarma_pulsado
        boton_alarma_pulsado = True
    enable_irq(s)

boton_adc.irq(handler=callback_adc, trigger=Pin.IRQ_FALLING)
boton_alarma.irq(handler=callback_alarma, trigger=Pin.IRQ_FALLING)

def callback(topic, msg):
    topic = topic.decode()
    msg = msg.decode()
    
    # También puedo comparar el topic entero pero así
    # se puede trabajar con las jerarquías
    # Split separa el string en una lista que tiene
    # cada elemento una jerarquía
    # "a/b/c/d".split("/") = [a, b, c, d]
    # el índice 0 va a quedar con un espacio en blanco
    subtopics = topic.split("/")
    
    if len(subtopics) < 4:
        print(f"Error con mensaje de {topic}: no está bien formado")
        return
    
    if subtopics[1] != ALUMNO:
        # no me corresponde
        return
    
    if subtopics[2] != "salidas":
        # nada más manejo salida, no me corresponde
        return
    
    if subtopics[3] == "led_verde":
        val = msg == "on"
        print(f"Escribiendo salida de led_verde a {val}")
        led_verde.value(val)
    elif subtopics[3] == "led_amarillo":
        val = msg == "on"
        print(f"Escribiendo salida de led_amarillo a {val}")
        led_amarillo.value(val)
    elif subtopics[3] == "led_rojo":
        val = msg == "on"
        print(f"Escribiendo salida de led_rojo a {val}")
        led_rojo.value(val)
    elif subtopics[3] == "servo":
        if not msg.isdigit():
            print(f"Error con mensaje {msg}: no es un número")
            return
        ang = int(msg)
        if ang < 0:
            ang = 0
        elif ang > 180:
            ang = 180
        d = int(50 + 50 * ang / 180)
        print(f"Escribiendo servo a ángulo {ang} con duty cycle {d}")
        servo.duty(d)
    elif subtopics[3] == "neopixel":
        if len(subtopics) != 5:
            # para ver si hay un 4to índice
            print(f"Error con mensaje de {topic}: falta el índice")
            return
        if not subtopics[4].isdigit():
            print(f"Error con mensaje {msg}: no es un número")
            return
        indice = int(subtopics[4])
        if indice < 0 or indice >= len(np):
            print(f"Error con mensaje de {topic}: fuera de rango")
            return
        
        color = msg.split(",")
        if len(color) != 3:
            print(f"Error con mensaje {msg}: debe tener 3 campos")
            return
        r, g, b = (int(color[0]),
                   int(color[1]),
                   int(color[2]))
        np[indice] = (r, g, b)
        print(f"Escribiendo NeoPixel índice {indice} con color {(r, g, b)}")
        np.write()
            
# para generar un nombre medio aleatorio
nombre = f"{ALUMNO}_{randint(1000,9999)}"
cliente = MQTTClient(nombre, "livra.local", port=1884)
print("Conectando a MQTT...")
cliente.connect()
cliente.set_callback(callback)
cliente.subscribe("#")
print("Conectado")

ult_mensaje_dht = 0

while True:
    cliente.check_msg()
    
    if boton_adc_pulsado:
        boton_adc_pulsado = False
        cliente.publish(f"/{ALUMNO}/entradas/nivel", str(adc.read()))
        
    if boton_alarma_pulsado:
        boton_alarma_pulsado = False
        cliente.publish(f"/{ALUMNO}/entradas/alarma", "ALARMA")
    
    if ticks_ms() - ult_mensaje_dht > 5000:
        ult_mensaje_dht = ticks_ms()
        dht.measure()
        print("Publicando temperatura y humedad")
        cliente.publish(f"/{ALUMNO}/entradas/temperatura", str(dht.temperature()))
        cliente.publish(f"/{ALUMNO}/entradas/humedad", str(dht.humidity()))
    
    sleep_ms(20)
