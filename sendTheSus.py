# send_the_sus.py

from microbit import *
import radio

sustunes = [
    'c2:4', 'c5:2', 'd#5:2', 'f5:2', 'f#5:2', 'f5:2', 'd#5:2', 'c5:2', 'R:4', 'a#4:1', 'd5:1', 'c5:2', 'R:4', 'g1:2', 'c2:4'
]

radio.on()

radio.config(channel=3)

while True:
    radio.send("WHEHN DHIY IHMPOWSTER IHZ SAHS")
    sleep(1500)
    
    for x in sustunes:
        radio.send(x)
        sleep(275)
        
    sleep(1500)
    radio.send("YUW AAR SAHS")
    sleep(10000)