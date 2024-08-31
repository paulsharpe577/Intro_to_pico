# Rui Santos & Sara Santos - Random Nerd Tutorials
# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-dc-motor-micropython/

from dcmotor import DCMotor
from machine import Pin, PWM
from time import sleep

frequency = 1000

pin1 = Pin(3, Pin.OUT)
pin2 = Pin(4, Pin.OUT)
enable = PWM(Pin(2), frequency)

pin3 = Pin(5, Pin.OUT)
pin4 = Pin(6, Pin.OUT)
enable2 = PWM(Pin(7), frequency)

dc_motor = DCMotor(pin1, pin2, enable)

dc_motor2 = DCMotor(pin3, pin4, enable2)

# Set min duty cycle (15000) and max duty cycle (65535) 
#dc_motor = DCMotor(pin1, pin2, enable, 15000, 65535)

try:
    print('Forward with speed: 75%')
    sleep(4)
    dc_motor.forward(75)
    dc_motor2.forward(75)
    sleep(3)
    dc_motor.stop()
    dc_motor2.stop()
    sleep(0.5)
    print('Backwards with speed: 60%')
    dc_motor.backwards(60)
    dc_motor2.backwards(60)
    sleep(3)
    print('Forward with speed: 30%')
    dc_motor.forward(30)
    dc_motor2.forward(30)
    sleep(2)
    dc_motor.stop()
    dc_motor2.stop()
    
except KeyboardInterrupt:
    print('Keyboard Interrupt')
    dc_motor.stop()
    dc_motor2.stop()
