
# Setting up a Python Project

![](packaging.png)

In this exercise, you create a structure to install and deploy your Python program easily.

## Package

Create a Python package with the following steps:

1. create a new folder `snake/`
2. move all Python files into that folder
3. rename the main application `main.py` to `__main__.py`
4. change the imports of `game.py` in `__main__.py` to `from snake.game import SnakeGame` .

You should now be able to run the game with:

    python snake

## Modules

Split `game.py` into two separate modules. 
Move the `Snake` class into a new file `player.py`.
Adjust all import statements accordingly.

## Virtural Environment

Create a virtual environment for the project.
You find an instruction to create an environment via `conda` on [academis.eu](http://www.academis.eu/software_engineering)

## Requirements

Create a file `requirements.txt` that lists all the dependencies on other packages.
The file should be in the main project folder (the one that contains `snake/`)
On Windows, you may add `windows-curses` there.

Also create a file `dev_requirements.txt`. Add the following packages:

    black
    isort
    pytest

To install packages from a requirements file type:

    pip install -r requirements.txt

## Sort import statements

The `isort` program sorts imports according to conventions:
First standard modules, then modules from pip-installed packages and finally your own modules.
You probably already have installed `isort` in the previous step.

Then run:

    isort *.py

## Setup script

Create a file `setup.py` in the main project folder (the one that contains `snake/`).
Use [this file](setup.py) as a template. Edit it to fill the gaps.

Now you can install the package for development with:

    python setup.py develop


## Style Checker

Install the **Pylance** plugin in VSCode to check Python style on the fly.
