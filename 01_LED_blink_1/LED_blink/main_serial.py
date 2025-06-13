"""
Serial LED control on Pico W
"""

import machine

# Set up LED on GPIO 15 (change pin if needed)
led = machine.Pin(15, machine.Pin.OUT)

print("Serial LED control started.")
print("Type '1' to turn LED ON, '0' to turn LED OFF.")

while True:
    cmd = input("Enter 1 or 0: ").strip()
    
    if cmd == '1':
        led.value(True)
        print("LED turned ON.")
    elif cmd == '0':
        led.value(False)
        print("LED turned OFF.")
    else:
        print("Invalid input. Please type '1' or '0'.")
