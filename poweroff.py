#!/bin/python3

from gpiozero import LED
from time import sleep

led = LED(17)

for i in range(0,5):
    led.on()
    sleep(0.1)
    led.off()
    sleep(0.1)
