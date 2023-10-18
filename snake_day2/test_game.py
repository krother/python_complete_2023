from game import SnakeGame
from unittest.mock import MagicMock, patch
import pytest

EMPTY_BOX = """
######
#    #
#    #
#    #
######""".strip()

BOX_WITH_FOOD_IN_CORNER = """
######
#*   #
#    #
#    #
######""".strip()


@pytest.fixture
@patch("random.randint", MagicMock(return_value=1))
def game():
    """prepare a snake game object for testing"""
    # fixture: a function that prepares test data
    # order of execution is important: patch is executed first
    return SnakeGame(size=(6, 5), start_pos=(1, 2))


def test_string_conversion_with_food(game):
    """string representation works"""
    # patch: replaces the randint function by a mock object that always returns 1
    #        after the test, put the original randint function back
    assert str(game) == BOX_WITH_FOOD_IN_CORNER


SIZES = [4, 9, 10, 100]


@pytest.mark.parametrize("playing_field_size", SIZES)
def test_create_game(playing_field_size):
    """game object is created"""
    # test parametrization: run the same test with different values
    s = SnakeGame(size=(playing_field_size, playing_field_size), start_pos=(5, 5))
    assert s.score == 0
    assert s.running


def test_string_conversion(game):
    """string representation works (without food)"""
    # the fixture 'game' is automatically called
    assert str(game).replace("*", " ") == EMPTY_BOX
