"""
Simple buzzer activation sound on pin 16
"""

from machine import Pin, PWM
from time import sleep

buzzerPIN=16
BuzzerObj = PWM(Pin(buzzerPIN))

def buzzer(buzzerPinObject,frequency,sound_duration,silence_duration):

    # Set duty cycle to a positive value to emit sound from buzzer
    buzzerPinObject.duty_u16(int(65536*0.1))
    # Set frequency
    buzzerPinObject.freq(frequency)
    # wait for sound duration
    sleep(sound_duration)
    # Set duty cycle to zero to stop sound
    buzzerPinObject.duty_u16(int(65536*0))
    # Wait for sound interrumption, if needed 
    sleep(silence_duration)


#set translation table from note to frequency
sol4=392
do5=523
dod5=554
re5=587
red5=622
mi5=659
fa5=698
fad5=739
sol5=784
sold5=830
la5=880
lad5=932
si5=987

buzzer(BuzzerObj,dod5,0.8,0.1)
buzzer(BuzzerObj,sold5,0.2,0.1)
buzzer(BuzzerObj,sold5,0.2,0.1)

#Deactivates the buzzer
BuzzerObj.deinit()

