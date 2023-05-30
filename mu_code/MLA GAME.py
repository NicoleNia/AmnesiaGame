# Write your code here :-)
# Write your code here :-)
import pygame

TITLE = "MLA"
HEIGHT = 800
WIDTH = 1300
state = "start"
gui_font = pygame.font.Font(None, 30)


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
       
