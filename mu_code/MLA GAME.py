# Write your code here :-)
# Write your code here :-)
import pygame
import usb_hid
from adafruit_circuitplayground.express import cpx
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
TITLE = "MLA"
HEIGHT = 800
WIDTH = 1300
state = "start"
gui_font = pygame.font.Font(None, 30)

while True:
    if cpx.button_a:
        kbd.send(Keycode.SHIFT, Keycode.A)  # Type capital 'A'
        while cpx.button_a:  # Wait for button to be released
            pass

    if cpx.button_b:
        kbd.send(Keycode.X)  # Type lowercase 'x'
        while cpx.button_b:  # Wait for button to be released
            pass
    if cpx.touch_A3:
        # Type 'Example Text' followed by Enter (a newline).
        layout.write("Example Text\n")
        while cpx.touch_A3:
            pass


def draw():
    screen.blit("background.jpg", (0, 0))

    if state == "start":
        screen.draw.text(
            "FADED MEMORIES",
            color="white",
            midtop=(WIDTH / 3.3, HEIGHT / 1.85 - 30),
            owidth=1,
            ocolor="black",
            fontsize=30,
        )

        screen.draw.text(
            "Press Difficulty Level to Start",
            color="white",
            midtop=(WIDTH / 3.3, HEIGHT / 1.85 + 50),
            owidth=1,
            ocolor="black",
            fontsize=20,
        )
