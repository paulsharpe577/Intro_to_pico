from machine import Pin, PWM
import time

# Buzzer on GPIO 15 (change as needed)
buzzer = PWM(Pin(16))

# Define note frequencies (in Hz)
NOTE_FREQS = {
    'C4': 262,
    'D4': 294,
    'E4': 330,
    'F4': 349,
    'G4': 392,
    'A4': 440,
    'B4': 494,
    'C5': 523,
    'REST': 0
}

def play_note(note, duration=500):
    freq = NOTE_FREQS.get(note.upper(), None)
    if freq is None:
        print(f"Note {note} not recognized, skipping.")
        return

    if freq == 0:
        # Rest note: just wait
        buzzer.duty_u16(0)
        time.sleep_ms(duration)
    else:
        buzzer.freq(freq)
        buzzer.duty_u16(32768)  # 50% duty cycle
        time.sleep_ms(duration)
        buzzer.duty_u16(0)

def play_sequence(sequence):
    notes = sequence.split()
    for note in notes:
        play_note(note)
        time.sleep_ms(50)  # short pause between notes

try:
    while True:
        seq = input("Enter notes (e.g. C4 D4 E4 REST F4): ")
        play_sequence(seq)
except KeyboardInterrupt:
    buzzer.deinit()
    print("\nGoodbye!")

