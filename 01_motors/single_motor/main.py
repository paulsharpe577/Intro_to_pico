

from dcmotor import DCMotor
from machine import Pin, PWM
from time import sleep

frequency = 1000

pin1 = Pin(3, Pin.OUT)
pin2 = Pin(4, Pin.OUT)
enable = PWM(Pin(2), frequency)

dc_motor = DCMotor(pin1, pin2, enable)

# Set min duty cycle (15000) and max duty cycle (65535) 
#dc_motor = DCMotor(pin1, pin2, enable, 15000, 65535)

try:
    print('Forward with speed: 50%')
    dc_motor.forward(50)
    sleep(2)
    dc_motor.stop()
    sleep(0.5)
    print('Backwards with speed: 100%')
    dc_motor.backwards(100)
    sleep(2)
    print('Forward with speed: 25%')
    dc_motor.forward(25)
    sleep(2)
    dc_motor.stop()
    
except KeyboardInterrupt:
    print('Keyboard Interrupt')
    dc_motor.stop()
