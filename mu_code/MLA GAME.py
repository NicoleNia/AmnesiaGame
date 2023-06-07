# Write your code here :-)
# Write your code here :-)
import pygame
import random
import time

TITLE = "MLA"
HEIGHT = 800
WIDTH = 1300
state = "start"
gui_font = pygame.font.Font(None, 30)
score = 0
mylist = ["red_back.jpg", "yellow_screen.jpg", "blue_screen.jpg," "green_screen.jpg"]
mylist_flag = False


def update():
    global mylist_flag
    if keyboard.A:
        print("A key")
        mylist_flag = True
        while keyboard.A:
            pass


def draw():
    if state == "start":
        screen.draw: " x_screen.jpg"
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

    if mylist_flag:
        print(random.choice(mylist))
        time.sleep(2)
