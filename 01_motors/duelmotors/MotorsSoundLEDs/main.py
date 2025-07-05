"""
Pico W firmware loaded - v1.23.0 (2024-06-02)
Moves motors forwards, turns then backwards
Uses a L298N
Requires dcmotor.py and buzzer.py
"""

from dcmotor import DCMotor
from machine import Pin, PWM
from time import sleep
from buzzer import Buzzer

led_forward = Pin(14, Pin.OUT)
led_back = Pin(15, Pin.OUT)

frequency = 1000

# Motor pins
in1 = Pin(3, Pin.OUT)
in2 = Pin(4, Pin.OUT)
enable = PWM(Pin(2), frequency)

in3 = Pin(5, Pin.OUT)
in4 = Pin(6, Pin.OUT)
enable2 = PWM(Pin(7), frequency)

# Buzzer setup
buzzer = Buzzer(16)

# Motor setup
dc_motor = DCMotor(in1, in2, enable)
dc_motor2 = DCMotor(in3, in4, enable2)

# LED helpers
def led_on(pin):
    pin.value(1)

def led_off(pin):
    pin.value(0)

try:
    sleep(4)
    
    # --- Forward ---
    print('Forward with speed: 75%')
    led_on(led_forward)
    led_off(led_back)
    buzzer.set_pitch(6000)  # Forward pitch
    buzzer.on()
    
    dc_motor.forward(75)
    dc_motor2.forward(75)
    sleep(3)
    
    dc_motor.stop()
    dc_motor2.stop()
    buzzer.off()
    led_off(led_forward)
    sleep(0.5)
    
    # --- Turn ---
    print('Turn with speed: 75%')
    led_off(led_forward)
    led_off(led_back)
    buzzer.set_pitch(7000)  # Turn pitch
    buzzer.on()
    
    dc_motor.backwards(75)
    dc_motor2.forward(75)
    sleep(3)
    
    dc_motor.stop()
    dc_motor2.stop()
    buzzer.off()
    sleep(0.5)
    
    # --- Backwards ---
    print('Backwards with speed: 30%')
    led_off(led_forward)
    led_on(led_back)
    buzzer.set_pitch(6000)  # Backward pitch
    buzzer.on()
    
    dc_motor.backwards(30)
    dc_motor2.backwards(30)
    sleep(2)
    
    dc_motor.stop()
    dc_motor2.stop()
    buzzer.off()
    led_off(led_back)

except KeyboardInterrupt:
    print('Keyboard Interrupt')
    dc_motor.stop()
    dc_motor2.stop()
    buzzer.off()
    led_off(led_forward)
    led_off(led_back)

