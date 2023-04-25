from adafruit_circuitplayground import cp
import time
cp.pixels.brightness = 0.3
cp.pixels[0] = 0x00FF00
cp.pixels[0] = (255, 0, 0)
cp.pixels[1] = (255, 0, 0)
cp.pixels[2] = (255, 0, 0)
cp.pixels[4] = (255, 0, 0)
cp.pixels[5] = (255, 0, 0)
cp.pixels[6] = (255, 0, 0)
cp.pixels[7] = (255, 0, 0)
cp.pixels[8] = (255, 0, 0)
cp.pixels[9] = (255, 0, 0)


while True:
    if cp.button_a:
        print("Button A pressed!")

while True:
    if cp.button_b:
        print("Button B pressed!")
