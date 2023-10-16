
# Object-Oriented Programming

![](duck_typing.png)

## A class as data containers

Create a class `Position` using the `pydantic` library for stricter type checking at runtime.
Install it with:

    pip install pydantic

Then use it:

    from pydantic import BaseModel

    class Position(BaseModel):
        x: int
        y: int

Create instances of the class. Try both correct and wrong types.

## Simplify code using a class

Use the Position class to replace the use of x and y in `game.py`.

## A class with methods

Convert the Snake class to a pydantic.BaseModel class as well.

Discuss the difference between *functions* and *methods*.
Also disuss what `self` is.

## Tail

Add a tail to the snake. Create a list of Positions as a new attribute of the Snake class.
Adjust the methods grow(), forward(), check_collision() and get_symbols() to take the tail into account.
