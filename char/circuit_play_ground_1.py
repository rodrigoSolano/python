# import CPX library
from adafruit_circuitplayground import cp
import time

red  = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
off = (0,0,0)

while True:
    cp.pixels.fill(red)
    time.sleep(0.5)
    cp.pixels.fill(green)
    time.sleep(0.5)
    cp.pixels.fill(blue)
    time.sleep(0.5)