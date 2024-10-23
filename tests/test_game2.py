# tests/test_game.py
import string
from longest_word.game import Game

class TestGame:

    def test_is_valid_with_new_grid(self):

        new_game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'EUREKA'
        new_game.grid = list(test_grid)

        assert new_game.is_valid(test_word) == True
        assert new_game.grid == list(test_grid)
