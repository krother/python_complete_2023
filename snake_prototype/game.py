from typing import Tuple, Iterable
import random


SNAKE = "O"
HEAD = "G"
WALL = "#"
FOOD = "*"

UP, DOWN, LEFT, RIGHT = range(1, 5)


class Snake:
    """A snake with a tail that grows"""

    # this class contains 3 bugs
    def __init__(self, head, direction=RIGHT):
        self.head = 5, 5
        self.direction = direction

    def forward(self):
        """Moves the snake one step ahead"""
        x, y = self.head
        if self.direction == RIGHT:
            self.head = x + 1, y
        elif self.direction == DOWN:
            self.head = y, x + 1
        else:
            self.head = x - 1, y

    def grow(self):
        ...

    def check_collision(self, size) -> bool:
        """Returns True if the snake hits an obstacle"""
        walls = set()
        for x in range(size[0]):
            walls.add((x, 0))
        for y in range(1, size[1] - 1):
            walls.add((0, y))
            walls.add((size[0] - 1, y))
        for x in range(size[0]):
            walls.add((x, size[1] - 1))
        return self.head in walls


class SnakeGame:
    def __init__(self, size: Tuple[int, int], start_pos: Tuple[int, int]):
        self.snake = Snake(head=start_pos)
        self._size = size
        self._food = None
        self.running = True
        self.add_random_food()
        self.score = 0

    def __repr__(self) -> str:
        """returns a string representation for convenience and debugging"""
        symbols = {(x, y): char for x, y, char in self.get_symbols()}
        return "".join(
            [
                ("".join([symbols.get((x, y), " ") for x in range(self.xsize)]) + "\n")
                for y in range(self._size[1])
            ]
        ).strip()

    @property
    def xsize(self) -> int:
        return self._size[0]

    def add_random_food(self) -> None:
        x, y = (random.randint(1, self.xsize - 2), random.randint(1, self._size[1] - 2))
        self._food = x, y

    def get_symbols(self) -> Iterable[Tuple[int, int]]:
        """Generates (x, y, char) tuples for everything tile to be drawn"""
        # walls
        for x in range(self.xsize):
            yield x, 0, WALL
        for y in range(1, self._size[1] - 1):
            yield 0, y, WALL
            yield self.xsize - 1, y, WALL
        for x in range(self.xsize):
            yield x, self._size[1] - 1, WALL
        # fruit
        if self._food:
            yield self._food[0], self._food[1], FOOD
        # player
        yield self.snake.head[0], self.snake.head[1], HEAD

    def set_direction(self, direction: int) -> None:
        self.snake.direction = direction

    def update(self) -> None:
        self.snake.forward()
        if self.snake.head == self._food:
            self.snake.grow()
            self.score += 1
            self.add_random_food()
        if self.snake.check_collision(self._size):
            self.running = False


if __name__ == "__main__":
    # test code
    game = SnakeGame(size=(10, 10), start_pos=(5, 5))
    print(game)
    print(game.get_symbols)
