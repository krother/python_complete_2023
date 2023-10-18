from typing import List, Literal  # builtin modules

from pydantic import BaseModel  # pip-installed things

from position import Position  # our own modules


Direction = Literal["UP", "DOWN", "LEFT", "RIGHT"]


class Snake(Player):
    """A snake with a tail that grows"""

    head: Position = Position(x=5, y=5)
    direction: Direction = "RIGHT"
    tail: List[Position] = []

    def forward(self):
        """Moves the snake one step ahead"""
        old_head = self.head
        if self.direction == "LEFT":
            self.head = Position(x=self.head.x - 1, y=self.head.y)
        elif self.direction == "RIGHT":
            self.head = Position(x=self.head.x + 1, y=self.head.y)
        elif self.direction == "UP":
            self.head = Position(x=self.head.x, y=self.head.y + 1)
        elif self.direction == "DOWN":
            self.head = Position(x=self.head.x, y=self.head.y - 1)
        if self.tail:
            self.tail.pop(0)  # remove first element
            self.tail.append(old_head)

    def grow(self):
        ...  # hey this is incomplete (Ellipsis)

    def check_collision(self, size) -> bool:
        """Returns True if the snake hits an obstacle"""
        walls = set()  # a collection of unique values {1, 2, 3}
        for x in range(size[0]):
            walls.add((x, 0))
        for y in range(1, size[1] - 1):
            walls.add((0, y))
            walls.add((size[0] - 1, y))
        for x in range(size[0]):
            walls.add((x, size[1] - 1))
        return (self.head.x, self.head.y) in walls
