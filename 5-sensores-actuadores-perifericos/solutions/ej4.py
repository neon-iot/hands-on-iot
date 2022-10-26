from machine import Pin, ADC

led_verde = Pin(15, Pin.OUT)
led_rojo = Pin(0, Pin.OUT)
led_amarillo = Pin(2, Pin.OUT)
adc = ADC(Pin(35), atten=ADC.ATTN_11DB)

while True:
#     valor_adc = adc.read_u16() / 65535
#     if valor_adc < 0.3:
#         led_rojo.on()
#         led_amarillo.off()
#         led_verde.off()
#     elif valor_adc < 0.6:
#         led_rojo.off()
#         led_amarillo.on()
#         led_verde.off()
#     else:
#         led_rojo.off()
#         led_amarillo.off()
#         led_verde.on()

    # alternativa
    valor_adc = adc.read_u16() / 65535
    led_rojo.value(valor_adc < 0.3)
    led_amarillo.value(0.3 <= valor_adc < 0.6)
    led_verde.value(0.6 <= valor_adc)
        
    
