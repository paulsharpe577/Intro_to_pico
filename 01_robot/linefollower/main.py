from dcmotor import DCMotor
from machine import Pin, PWM
from time import sleep

# Motor setup
frequency = 1000

# Left motor
in1 = Pin(3, Pin.OUT)
in2 = Pin(4, Pin.OUT)
enable = PWM(Pin(2), freq=frequency)

# Right motor
in3 = Pin(5, Pin.OUT)
in4 = Pin(6, Pin.OUT)
enable2 = PWM(Pin(7), freq=frequency)

dc_motor = DCMotor(in1, in2, enable)
dc_motor2 = DCMotor(in3, in4, enable2)

# Sensor setup
left_sensor = Pin(26, Pin.IN)
right_sensor = Pin(27, Pin.IN)

# Speed settings
normal_speed = 40
turn_speed = 30

try:
    while True:
        left = left_sensor.value()
        right = right_sensor.value()

        # Case 1: Both sensors see white - go forward
        if left == 1 and right == 1:
            dc_motor.forward(normal_speed)
            dc_motor2.forward(normal_speed)
            sleep(0.05)
            dc_motor.stop()
            dc_motor2.stop()
            sleep(0.1)

        # Case 2: Left sees black - turn left
        elif left == 0 and right == 1:
            dc_motor.forward(turn_speed)
            dc_motor2.stop()
            sleep(0.05)
            dc_motor.stop()
            sleep(0.1)

        # Case 3: Right sees black - turn right
        elif left == 1 and right == 0:
            dc_motor.stop()
            dc_motor2.forward(turn_speed)
            sleep(0.05)
            dc_motor2.stop()
            sleep(0.1)

        # Case 4: Both see black - stop
        else:
            dc_motor.stop()
            dc_motor2.stop()
            sleep(0.2)

except KeyboardInterrupt:
    dc_motor.stop()
    dc_motor2.stop()
    print("Stopped")

