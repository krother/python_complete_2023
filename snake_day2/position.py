"""
A position in a 2D game

pydantic:
- creates a constructor for us
- does type validation
- instances can be printed as strings easily
"""
from pydantic import BaseModel


class Position(BaseModel):
    x: int
    y: int


origin = Position(x=0, y=0)
print(origin)

# wrong = Position(x="7", y=[7])
