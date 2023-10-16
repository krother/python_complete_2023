"""
At the end of the game, a high score list should be printed on the console containing
names of players and their scores.

What data structure would you use to store the entire high score list?

Define an according type `Highscores` using type annotations.

Then implement a function with the following signature:
"""
from typing import Dict, Union

# from operator import itemgetter
import json

Highscores = Dict[str, int]


def display_high_scores(high_scores: Highscores) -> Union[str, None]:
    """formats the high scores for printing"""
    if not high_scores:
        return None
    # 1. get all values from the dictionary
    data = [(score, name) for name, score in high_scores.items()]
    # 2. sort them
    data.sort(reverse=True)
    # OR data.sort(reverse=True, key=itemgetter(1))
    # OR data.reverse()
    # 3. put them into a string
    result = "----------------- HIGH SCORES ---------------------"
    for position, (score, name) in enumerate(data, start=1):
        result += f"\n{position:2}. {name:20}{score:20}"
    return result


def read_highscores() -> Highscores:
    """read the high scores from a JSON file"""
    filename = "highscores.json"
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def write_highscores(highscores: Highscores) -> None:
    """write the high scores to a JSON file"""
    filename = "highscores.json"
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(highscores, file)


scores = read_highscores()

# enter score
player_score = int(input("enter your score: "))
player_name = input("enter your name: ")
scores[player_name] = player_score  # add a new key:value pair to a dict

print(display_high_scores(scores))
write_highscores(scores)
