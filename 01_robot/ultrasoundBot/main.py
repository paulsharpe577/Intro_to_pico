"""
Pico W firmware loaded - v1.23.0 (2024-06-02)
Ultrasound robot- avoids objects
..
"""
#Imports
from dcmotor import DCMotor
from machine import Pin, PWM
from random import seed
import random
import utime

#A sleep to stop brownout of board
utime.sleep(2)

# Motor setup
seed(1)
frequency = 1000
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

#Buzzer setup
buzzerPIN=16
BuzzerObj = PWM(Pin(buzzerPIN))

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
   
def buzzer(buzzerPinObject,frequency,sound_duration,silence_duration):
    # Set duty cycle to a positive value to emit sound from buzzer
    buzzerPinObject.duty_u16(int(65536*0.1))
    # Set frequency
    buzzerPinObject.freq(frequency)
    # wait for sound duration
    utime.sleep(sound_duration)
    # Set duty cycle to zero to stop sound
    buzzerPinObject.duty_u16(int(65536*0))
    # Wait for sound interrumption, if needed 
    utime.sleep(silence_duration)
    
def buzz():
    buzzer(BuzzerObj,554,0.8,0.1)
    buzzer(BuzzerObj,830,0.2,0.1)
    buzzer(BuzzerObj,830,0.2,0.1)
    BuzzerObj.deinit()

buzz()

while True:
    ultra()
    randomInt = random.uniform(0.1, 3)
    randomTurn = random.randint(0, 1)
    if round(distance) <20:
        dc_motor.stop()
        dc_motor2.stop()
        utime.sleep(1)   
        dc_motor.backwards(40)
        dc_motor2.backwards(40)
        utime.sleep(1)
        if randomTurn == 0:
            dc_motor.forward(40)
            dc_motor2.backwards(40)
            utime.sleep(randomInt)
        else:
            dc_motor.backwards(40)
            dc_motor2.forward(40)
            utime.sleep(randomInt)
    else:
        dc_motor.forward(40)
        dc_motor2.forward(40)
        #print("Motors forward")
        #print("The distance from object is ",round(distance),"cm")
    utime.sleep(0.2)    
    
