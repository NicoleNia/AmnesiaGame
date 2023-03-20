# Write your code here :-)
TITLE = "MLA"
WIDTH = 1000
HEIGHT = 500
state = "start"


def draw():
    screen.blit("mlsbackg.png", (0, 0))

    if state == "start":
        screen.draw.text(
            "Welcome to the Memory Loss Awareness Game!",
            color="white",
            midtop=(WIDTH / 2, HEIGHT / 2 - 50),
            owidth=1,
            ocolor="blue",
            fontsize=50,
        )

        screen.draw.text(
            "Press Difficulty Level to Start",
            color="white",
            midtop=(WIDTH / 2, HEIGHT / 2 + 50),
            owidth=1,
            ocolor="blue",
            fontsize=30,
        )
