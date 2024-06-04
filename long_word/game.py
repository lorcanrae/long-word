# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import string
import random
import requests


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

        # Check if word is in dictionary
        # url = f"https://dictionary.lewagon.com/{word}"
        # response = requests.get(url).json()
        # if not response["found"]:
        #     return False

        return self.__check_dictionary(word)

    @staticmethod
    def __check_dictionary(word):
        response = requests.get(f"https://dictionary.lewagon.com/{word}").json()
        return response['found']


if __name__ == "__main__":
    game = Game()
    print(game.grid)  # --> OQUWRBAZE
    my_word = "BAROQUE"
    game.is_valid(my_word)  # --> True
