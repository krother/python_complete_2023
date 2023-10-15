
# Data Structures and Functions

## Define your own Types

Look at the type annotations in the class `game.SnakeGame`.
The type definition for x/y coordinates repeats several times.
Create a new type definition:

    Position = Tuple[int, int]

And place `Position` in the function headers instead of the longer expression with `Tuple[...].

Make sure the program still runs.

## Complete Type Annotations

Complete the type annotations in all function headers for the `Snake` class.

## Literals

Create a Literal type for the directions in `game.py`, allowing string values:

    from typing import Literal

    Direction = Literal["up", "down", ...]

and replace the occurence of the integer constants `UP`, `DOWN` etc. wherever they occur.

## Extract a function

Find a piece of almost duplicate code in `game.py`.
Move the redundant piece into a function.

## Types for a high score list

At the end of the game, a high score list should be printed on the console containing
names of players and their scores.
What data structure would you use to store the entire high score list?

Define an according type `Highscores` using type annotations.

Then implement a function with the following signature:

    def display_high_scores(high_scores: Highscores) -> None:
        """prints high scores to the terminal"""
        ...
