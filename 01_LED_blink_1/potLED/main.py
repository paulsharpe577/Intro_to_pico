from machine import Pin, PWM, ADC
import time

# Setup LED on GP15 as PWM output
led = PWM(Pin(15))
led.freq(1000)

# Setup potentiometer on GP26 (ADC0)
pot = ADC(26)

while True:
    pot_value = pot.read_u16()  # 0 to 65535
    led.duty_u16(pot_value)     # Set LED brightness
    time.sleep(0.01)            # Small delay for stability

