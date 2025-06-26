from buzzer import Buzzer
import time

buzzer = Buzzer(16)

while True:
    buzzer.beep(0.1, freq=2000)
    time.sleep(0.5)
    
    buzzer.beep(0.1, freq=3000)
    time.sleep(0.5)
    
    buzzer.beep(0.1, freq=4000)
    time.sleep(0.5)

