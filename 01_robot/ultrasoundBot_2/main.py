"""
Pico W firmware loaded - v1.23.0 (2024-06-02)
Ultrasound robot - looks around by turning left/right and chooses longest path
"""
from dcmotor import DCMotor
from machine import Pin, PWM
import utime
import random

utime.sleep(2)  # prevent brownout

# Motor setup
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
trigger = Pin(12, Pin.OUT)
echo = Pin(13, Pin.IN)

# Buzzer setup
buzzerPIN = 16
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
    distance = (timepassed * 0.0343) / 2
    return distance

def buzzer(buzzerPinObject, frequency, sound_duration, silence_duration):
    buzzerPinObject.duty_u16(int(65536 * 0.1))
    buzzerPinObject.freq(frequency)
    utime.sleep(sound_duration)
    buzzerPinObject.duty_u16(0)
    utime.sleep(silence_duration)

def buzz():
    buzzer(BuzzerObj, 554, 0.4, 0.1)
    buzzer(BuzzerObj, 830, 0.2, 0.1)
    buzzer(BuzzerObj, 830, 0.2, 0.1)
    BuzzerObj.deinit()

buzz()

def look_around():
    # Reverse slightly to give room
    dc_motor.backwards(40)
    dc_motor2.backwards(40)
    utime.sleep(0.4)

    # Look left
    dc_motor.backwards(40)
    dc_motor2.forward(40)
    utime.sleep(0.5)
    left_dist = ultra()

    # Return to centre
    dc_motor.forward(40)
    dc_motor2.backwards(40)
    utime.sleep(0.5)

    # Look right
    dc_motor.forward(40)
    dc_motor2.backwards(40)
    utime.sleep(0.5)
    right_dist = ultra()

    # Return to centre again
    dc_motor.backwards(40)
    dc_motor2.forward(40)
    utime.sleep(0.5)

    print("Left:", round(left_dist), "cm | Right:", round(right_dist), "cm")

    # Choose direction with more space
    if left_dist > right_dist:
        print("Turning left")
        dc_motor.backwards(40)
        dc_motor2.forward(40)
        utime.sleep(0.5)
    else:
        print("Turning right")
        dc_motor.forward(40)
        dc_motor2.backwards(40)
        utime.sleep(0.5)

    # Move forward again
    dc_motor.forward(40)
    dc_motor2.forward(40)

# Main loop
while True:
    distance = ultra()
    if distance < 20:
        dc_motor.stop()
        dc_motor2.stop()
        utime.sleep(0.2)
        look_around()
    else:
        dc_motor.forward(40)
        dc_motor2.forward(40)
    utime.sleep(0.1)

