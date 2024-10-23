import requests

class Game:

    def __init__(self) -> list:
        self.grid = self.generate_grid()

    def generate_grid(self):
        return ['O', 'Q', 'U', 'W', 'R', 'B', 'A', 'Z', 'E']

    def __str__(self):
        return ''.join(self.grid)

    def is_valid(self, word: str) -> bool:
        word = word.upper()
        grid_list = self.grid

        for letter in word:
            if letter in grid_list:
                return True
            else:
                return False
        return self.__check_dictionary(word)

    @staticmethod
    def __check_dictionary(word):
        response = requests.get(f"https://dictionary.lewagon.com/{word}")
        json_response = response.json()
        return json_response['found']

if __name__ == "__main__":
    game = Game()
    print(game)
    my_word = "BAROQUE"
    game.is_valid(my_word)
    print(game.is_valid(my_word))
