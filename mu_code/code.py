from adafruit_circuitplayground import cp
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
cp.adjust_touch_threshold(200)
cp.pixels.brightness = 0.3

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
OFF = (0, 0, 0)
score = 0


def turn_on_leds():
    for pixel_num in range(0, 4):
        cp.pixels[pixel_num] = RED
        time.sleep(0.2)

    for pixel_num in range(2, 6):
        cp.pixels[pixel_num] = BLUE
        time.sleep(0.2)
    for pixel_num in range(5, 9):
        cp.pixels[pixel_num] = GREEN
        time.sleep(0.2)
    for pixel_num in range(7, 9):
        cp.pixels[pixel_num] = YELLOW
        time.sleep(0.2)


def gradual_light_up(color, start, stop):
    cp.pixels.fill(OFF)
    for pixel_num in range(start, stop):
        cp.pixels[pixel_num] = color
        time.sleep(5)


def level_1_seq():
    gradual_light_up(RED, 0, 3)
    if cp.touch_A2:
        print("Touched pad A1")
        cp.pixels.fill(OFF)
        while cp.touch_A2:
            pass

    gradual_light_up(GREEN, 5, 9)
    if cp.touch_A3:
        print("Touched pad A3")
        cp.pixels.fill(OFF)
        while cp.touch_A3:
            pass
    gradual_light_up(BLUE, 2, 6)
    if cp.touch_A6:
        print("Touched pad A4")
        cp.pixels.fill(OFF)
        while cp.touch_A6:
            pass

    gradual_light_up(YELLOW, 7, 10)
    if cp.touch_A7:
        print("Touched pad A6")
        cp.pixels.fill(OFF)
        while cp.touch_A7:
            pass


while True:

    if cp.button_a:
        print("Button A pressed!")
        turn_on_leds((RED, BLUE, GREEN, YELLOW))
        time.sleep(1.0)
        cp.pixels.fill(OFF)
        while cp.button_a:
            pass

    if cp.button_b:
        print("Button B pressed!")
        level_1_seq()
        while cp.button_b:
            pass

    if cp.touch_A2:
        print("Touched pad A2")
        kbd.send(Keycode.S)
        cp.pixels.fill(OFF)
        while cp.touch_A2:
            pass

    if cp.touch_A3:
        print("Touched pad A3")
        kbd.send(Keycode.D)
        cp.pixels.fill(OFF)
        while cp.touch_A3:
            pass

    if cp.touch_A6:
        print("Touched pad A6")
        kbd.send(Keycode.Z)
        cp.pixels.fill(OFF)
        while cp.touch_A6:
            pass

    if cp.touch_A7:
        print("Touched pad A7")
        kbd.send(Keycode.X)
        cp.pixels.fill(OFF)
        while cp.touch_A7:
            pass
