from long_word.game import Game
import string


class TestGame:

    def test_game_initialization(self):
        # setup
        game = Game()

        # exercise
        grid = game.grid

        # verify
        assert isinstance(grid, list), "Make sure that Game.grid attribute is a list"
        assert len(grid) == 9
        for letter in grid:
            assert letter in string.ascii_uppercase

        # teardown

    def test_empty_word_is_invalid(self):
        # setup
        new_game = Game()

        # verify
        assert new_game.is_valid("") is False

    def test_is_valid(self):
        # setup
        new_game = Game()
        test_grid = "OQUWRBAZE"
        test_word = "BAROQUE"

        # exercise
        new_game.grid = list(test_grid)

        # verify
        assert new_game.is_valid(test_word) is True

        # teardown
        assert new_game.grid == list(test_grid)

    def test_is_invalid(self):
        # setup
        new_game = Game()
        test_grid = "OQUWRBAZE"
        test_word = "SANDWICH"

        # exercise
        new_game.grid = list(test_grid)

        # verify
        assert new_game.is_valid(test_word) is False

        # teardown
        assert new_game.grid == list(test_grid)
