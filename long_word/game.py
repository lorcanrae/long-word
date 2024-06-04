# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import string
import random


class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        if not word:
            return False
        letters = self.grid.copy()
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return True


if __name__ == "__main__":
    game = Game()
    print(game.grid)  # --> OQUWRBAZE
    my_word = "BAROQUE"
    game.is_valid(my_word)  # --> True
