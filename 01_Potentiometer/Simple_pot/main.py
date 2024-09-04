"""
POT range from 0 to 65535 so that it behaves the same as ADC on other MicroPython microcontrollers.

It has five ADC channels, but only four are accessible on the GPIOs: GPIO26, GPIO27, GPIO28, and GPIO29.

The first three GPIOs (26, 27, and 28) can be used to read voltage from peripherals, while GPIO29
can be utilized to measure the voltage level of the VSYS supply on the Raspberry Pi Pico board
(VSYS is the input voltage that powers the board).

Connect POT to 3.3v supply, connected to GPIO 26
"""

#Imports
from machine import Pin, ADC
from time import sleep

#Pins
pot = ADC(Pin(26))

def ScalePercent(volt):
    percent = (volt/3.3)*100
    return int(percent)

while True:
  pot_value = pot.read_u16() # read value, 0-65535 across voltage range 0.0v - 3.3v
  print(pot_value, "(Raw 16 bit number)")
  pot_valueV = pot.read_u16() * 3.3 / 65535
  print (round(pot_valueV, 1), "Volts")
  percentPot = ScalePercent(pot_valueV)
  print(str(percentPot) + "%")
  sleep(0.1)

