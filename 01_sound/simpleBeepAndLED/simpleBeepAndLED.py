from machine import Pin, PWM
from time import sleep, sleep_ms

# Setup: Buzzer on GP16, LED on GP15
buzzer = PWM(Pin(16))
led = Pin(15, Pin.OUT)

# Note frequencies (Hz)
notes = {
    'C': 523,
    'D': 587,
    'E': 659,
    'F': 698,
    'G': 784,
    ' ': 0,  # Rest
}

# Simple tune
tune = [
    ('C', 0.2), ('E', 0.2), ('G', 0.4),
    ('F', 0.2), ('E', 0.2), ('D', 0.4),
    ('C', 0.2), ('D', 0.2), ('E', 0.4),
    ('C', 0.6),
]

# Play the tune
for note, length in tune:
    sound = notes[note]
    
    # Flash LED briefly
    led.on()
    sleep_ms(50)      # short blink
    led.off()

    if sound == 0:
        buzzer.duty_u16(0)  # pause
    else:
        buzzer.freq(sound)
        buzzer.duty_u16(3000)
    
    sleep(length)
    buzzer.duty_u16(0)

# Cleanup
buzzer.deinit()

