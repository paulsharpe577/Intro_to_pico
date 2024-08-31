"""
Pico W firmware loaded - v1.23.0 (2024-06-02)
Blinks and LED on pin 15
"""

import machine
import time

led = machine.Pin(15, machine.Pin.OUT) #configure GPIO-15 Pin as an output pin and create and led object for Pin class

while True:
  led.value(True)  #turn on the LED
  time.sleep(1)   #wait for one second
  led.value(False)  #turn off the LED
  time.sleep(1)   #wait for one second
