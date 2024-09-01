"""
Pico W firmware loaded - v1.23.0 (2024-06-02)
Ultrasound HC-SR04 sensor working on Pico 3.3V
Trig pin 12
Echo pin 13
"""

from machine import Pin
import utime
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
   distance = (timepassed * 0.0343) / 2
   print("The distance from object is ",distance,"cm")
while True:
   ultra()
   utime.sleep(0.2)
