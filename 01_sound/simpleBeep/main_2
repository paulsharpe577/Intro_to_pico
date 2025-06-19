# Step 1: Get the tools we need
from machine import Pin, PWM  # PWM lets us make sound with the buzzer
from time import sleep        # sleep lets us wait between notes

# Step 2: Set up the buzzer on pin 16
buzzer = PWM(Pin(16))  # This tells the Pico where the buzzer is

# Step 3: Notes and their sound (how high or low the beep is)
notes = {
    'C': 523,
    'D': 587,
    'E': 659,
    'F': 698,
    'G': 784,
    ' ': 0,  # This is a rest (a pause)
}

# Step 4: The tune 
tune = [
    ('C', 0.2), ('E', 0.2), ('G', 0.4),
    ('F', 0.2), ('E', 0.2), ('D', 0.4),
    ('C', 0.2), ('D', 0.2), ('E', 0.4),
    ('C', 0.6),
]

# Step 5: Play each note in the tune
for note, length in tune:
    sound = notes[note]
    if sound == 0:
        buzzer.duty_u16(0)  # turn off sound for a pause
    else:
        buzzer.freq(sound)      # set how high the beep is
        buzzer.duty_u16(3000)   # set how loud the beep is
    sleep(length)  # wait for the length of the note

# Step 6: Turn off the buzzer when we're done
buzzer.duty_u16(0)
buzzer.deinit()
