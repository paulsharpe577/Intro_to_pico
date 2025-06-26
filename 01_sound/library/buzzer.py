from machine import Pin, PWM
import time

class Buzzer:
    def __init__(self, pin_number):
        self.pwm = PWM(Pin(pin_number))
        self.pwm.duty_u16(0)  # Start silent
        self.pwm.freq(3000)   # Default pitch

    def on(self, volume=2000):
        self.pwm.duty_u16(volume)

    def off(self):
        self.pwm.duty_u16(0)

    def set_pitch(self, freq):
        self.pwm.freq(freq)

    def beep(self, duration=0.1, volume=2000, freq=None):
        if freq:
            self.set_pitch(freq)
        self.on(volume)
        time.sleep(duration)
        self.off()

