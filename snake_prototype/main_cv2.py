"""
Snake User Interface with OpenCV2

Installation:

* open a terminal (Ctrl+R + cmd)
* check your pip version with `python -m pip --version` , should be >=19.3
* intall with `python -m pip install opencv-contrib-python`

also see: https://pypi.org/project/opencv-python/
"""
import time

import cv2
import numpy as np

from game import SnakeGame
from game import UP, DOWN, LEFT, RIGHT

# AWSD should work on all operating systems
KEY_COMMANDS = {"a": LEFT, "d": RIGHT, "w": UP, "s": DOWN}

# size of the playing field
XSIZE, YSIZE = 25, 20
TILE_SIZE = 32

# game delay (higher=slower)
SPEED = 20

COLORS = {
    " ": (0, 0, 0),
    "G": (0, 255, 0),
    "O": (0, 255, 0),
    "*": (0, 0, 255),
    "#": (128, 0, 128),
}


def draw(game):
    """draws characters for playing field, fruit and snake"""
    frame = np.zeros((YSIZE * TILE_SIZE, XSIZE * TILE_SIZE, 3), np.uint8)
    for x, y, char in game.get_symbols():
        color = COLORS.get(char, COLORS[" "])
        frame[
            y * TILE_SIZE : (y + 1) * TILE_SIZE, x * TILE_SIZE : (x + 1) * TILE_SIZE
        ] = color
    return frame


if __name__ == "__main__":
    game = SnakeGame((XSIZE, YSIZE), (3, 10))
    delay = 1

    while game.running:
        # update in regular intervals
        delay -= 1
        if delay == 0:
            delay = SPEED
            game.update()
            frame = draw(game)
            cv2.imshow("frame", frame)

        # move the player
        key = chr(cv2.waitKey(1) & 0xFF)
        if key == "q":
            game.running = False
        if key in KEY_COMMANDS:
            game.set_direction(KEY_COMMANDS[key])

        time.sleep(0.01)

    # game over
    time.sleep(1)
    cv2.destroyAllWindows()
