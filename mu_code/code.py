# Write your code here :-)
# Write your code here :-)
from adafruit_circuitplayground import cp
import time

cp.adjust_touch_threshold(200)
cp.pixels.brightness = 0.3
cp.pixels[0] = 0x00FF00

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
OFF = (0, 0, 0)
score = 0 

def turn_on_leds(color):
    for pixel_num in range(0, 4):
        cp.pixels[pixel_num] = RED
        time.sleep(0.2)

    for pixel_num in range(2, 6):
        cp.pixels[pixel_num] = BLUE
        time.sleep(0.2)
    for pixel_num in range(5, 9):
        cp.pixels[pixel_num] = GREEN
        time.sleep(0.2)
    for pixel_num in range(7, 10):
        cp.pixels[pixel_num] = YELLOW
        time.sleep(0.2)


def turn_off_all_leds(OFF):
    for pixel_num in range(0, 10):
        cp.pixels[pixel_num] = OFF
        
def level_1_seq():
    for cp.pixels[pixel_num] = RED
    
    
while True:
    if cp.button_a:
        print("Button A pressed!")
        turn_on_leds((RED, BLUE, GREEN, YELLOW))
        time.sleep(1.0)
        turn_off_all_leds(OFF)
        global score = 0

    if cp.button_b:
        print("Button B pressed!")
        level_1_seq()
    if cp.touch_A1:
        print("Touched pad A1")
    if cp.touch_A2:
        print("Touched pad A2")
        
    if cp.touch_A3:
        print("Touched pad A3")
        
    if cp.touch_A6:
        print("Touched pad A6")
        turn_on_leds(YELLOW)
    if cp.touch_A7:
        print("Touched pad A7")
