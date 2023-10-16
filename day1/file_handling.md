
# File Handling

![](files.png)

## Load a High Score List

At the end of the game, a high score list should be printed on the console.
Create a JSON file that contains the high scores in the structure you defined earlier.

Put the following phrases in the right order:

    file = open("high_scores.json", "r")

    display_high_scores(high_scores)

    high_scores = json.load(file)

    import json


## Save the High Score List

If the score is high enough to enter the list, the player enters their name.
The high score list should be saved to a file.
Complete the following phrases:

    name = input(...)

    high_scores[...] = ...
    
    json.dump(..., file)
    
    file = open(..., 'w')
    
    
## Other file types

What modules/libraries would you use to read/write data of the following types?

* CSV
* toml
* yml
* plain text
* arbitrary Python objects

See [Python Package Examples](https://github.com/krother/Python3_Package_Examples).

## Environment Variable

Use an environment variable to configure the name of the high score file.
Include the following code:

    import os

    high_score_filename = os.environ.get("SNAKE_HIGHSCORE_FILE")
