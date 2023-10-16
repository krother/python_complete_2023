# Exception Handling

![](apples.png)

## Raise errors
Add a validation function to the `SnakeGame` class:

    def validate(self):
        """raises an error if the starting position is not inside the playing field"""
        if ...
            raise Exception("starting position is not in the playing field")

Call the validation function when a new game is started

## Catch the exception

Add a `try.. except` block to the module `__main__.py` that gently exits the program with an error message
if an Exception occurs:

    try:
       # call the game code
       ...
    except:
       # gently exit with an error message instead of the full traceback
       ...
       

## Define your own Exception

Define your own exception so that the `try..except` block does not catch every possible Exception:

    class SnakeValidationError(Exception):
        pass

Adjust the `raise` and `except` statements accordingly.

## Test for the Exception

Write a test that makes sure the exception is raised:

    import pytest

    def test_wrong_parameters():
        with pytest.raises(Snake)
