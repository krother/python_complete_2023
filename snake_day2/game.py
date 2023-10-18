from typing import Tuple, Iterable, List, Literal
import random

from position import Position
from snake import Snake


SNAKE = "O"
HEAD = "G"
WALL = "#"
FOOD = "*"


class SnakeGame:
    def __init__(self, size: Position, start_pos: Position):
        # type annotation : signals what the programmer intends
        #  python ignores them, but we can use an extra program to check types
        self.snake = Snake(head=start_pos)
        self._size = size
        self._food = None
        self.running = True
        self.add_random_food()
        self.score = 0

    def __repr__(self) -> str:
        """returns a string representation for convenience and debugging"""
        symbols = {
            (x, y): char for x, y, char in self.get_symbols()
        }  # dict comprehension
        return "".join(
            [
                ("".join([symbols.get((x, y), " ") for x in range(self.xsize)]) + "\n")
                for y in range(self._size[1])
            ]
        ).strip()

    @property  # decorator
    def xsize(self) -> int:
        return self._size[0]

    def add_random_food(self) -> None:
        x, y = (random.randint(1, self.xsize - 2), random.randint(1, self._size[1] - 2))
        self._food = x, y

    def get_symbols(self) -> Iterable[Tuple[int, int]]:
        """Generates (x, y, char) tuples for everything tile to be drawn"""
        # walls
        # yield: generator function
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
    # Java : public static void main()
    # C : int main()
    # Python: executed when you run this file directly: 'python game.py'
    # Python: not executed when you import this file
    # test code
    game = SnakeGame(size=Position(x=10, y=10), start_pos=Position(x=5, y=5))
    print(game)
