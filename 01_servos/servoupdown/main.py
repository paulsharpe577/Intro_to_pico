#Imports
from servo import Servo
import time

#Pin setup
sg90_servo = Servo(pin=28)  

while True:
        for x in range(180, 0, -1):
            sg90_servo.move(x)
            print(x)
            time.sleep(0.01)
        for x in range (0, 180):
            sg90_servo.move(x)
            print(x)
            time.sleep(0.01)
