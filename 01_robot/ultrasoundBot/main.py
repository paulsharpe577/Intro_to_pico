"""
Pico W firmware loaded - v1.23.0 (2024-06-02)
"""
from dcmotor import DCMotor
from time import sleep
from machine import Pin, PWM
import utime
frequency = 1000

# Motor setup
in1 = Pin(3, Pin.OUT)
in2 = Pin(4, Pin.OUT)
enable = PWM(Pin(2), frequency)

in3 = Pin(5, Pin.OUT)
in4 = Pin(6, Pin.OUT)
enable2 = PWM(Pin(7), frequency)

dc_motor = DCMotor(in1, in2, enable)
dc_motor2 = DCMotor(in3, in4, enable2)

# Ultrasound setup
distance = 0
trigger = Pin(12, Pin.OUT)
echo = Pin(13, Pin.IN)

def ultra():
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   global distance
   distance = (timepassed * 0.0343) / 2
   #print("The distance from object is ",round(distance),"cm")
while True:
    ultra()
    if round(distance) <10:
        dc_motor.backwards(40)
        dc_motor2.backwards(40)
        print("Motors backwards")
        print("The distance from object is ",round(distance),"cm")
    else:
        dc_motor.forward(40)
        dc_motor2.forward(40)
        print("Motors forward")
        print("The distance from object is ",round(distance),"cm")
    utime.sleep(0.2)    
    
