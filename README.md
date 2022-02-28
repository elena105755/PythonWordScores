Scrabble™ is a long-established and popular word game in many different languages.The object of the game is to build valid words (for this exercise words are valid if they are present in the wordlist.txt file supplied) from a set of letter (tiles) that the player holds.

Each letter carries a different score value based on its frequency in the language. For example in English vowels such as A and E score only 1 point but less frequent letters such as K and J score 5 and 8 points respectively. The score for any particular word is the sum of the values of all the letters that make up the word. So for example:the word cabbage scores C3 + A1 + B3 + B3 + A1 + G2 + E1 = 14 points. The score values of letters in English are shown in the letterValues.txt file (also supplied).

Virtual environment handled with Python Poetry. Useful Poetry commands:

Note: Python Poetry can be installed using brew: `brew install poetry`

`poetry shell` - create/activate virtual environmnement

`poetry run python3 src/highscoringwords.py` - runs main script

`poetry run python3 -m unittest test/test_highscoringwords.py` - runs unit tests
