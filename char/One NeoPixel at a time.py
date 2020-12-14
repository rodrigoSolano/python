from adafruit_circuitplayground.express import cpx
import time 

blue = (0,0,255)
red = (255,0,0)

while True:
    for i in range(0,10):
        cpx.pixels[i] = red
        time.sleep(0.5)

    time.sleep(0.5)

    for i in range(0,10): 
        cpx.pixels[i] = blue
        time.sleep(0.5)
