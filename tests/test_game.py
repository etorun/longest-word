# tests/test_game.py
import string
from longest_word.game import Game

class TestGame:

    def test_game_initialization(self):
        # setup
        game = Game()

        # exercise
        grid = game.grid

        # verify
        assert isinstance(grid, list)
        assert len(grid) == 9
        for letter in grid:
                assert letter in string.ascii_uppercase

    def test_word_in_grid(self):
        game = Game()
        grid = game.grid
        assert game.is_valid('BAROQUE') == True, 'Word (all letters) is in the grid'

    def test_word_not_in_grid(self):
        game = Game()
        grid = game.grid
        assert game.is_valid('Phone') == False, 'Word (all letters) is NOT in the grid'
