"""Player vs Player class."""
from Player import Player
from colors import colors
import pickle


class player_vs_player:
    """This is a class for a player vs player game."""

    def __init__(self):
        """Initialize the player vs player game."""
        self.player = Player("", 0)

    def save_game(player_dict):
        """Save the game."""
        try:
            with open("save_game.pkl", "wb") as file:
                pickle.dump(player_dict, file)
        except FileNotFoundError:
            print("Error, file not found.")

    def load_game():
        try:
            with open("save_game.pkl", "rb") as file:
                loaded = pickle.load(file)
        except FileExistsError:
            print("Error")
        print(loaded)

    def two_player_game(self, name_1, name_2):
        """Simulate a two player game of Pig."""
        print(">> Welcome to a game of Pig! <<\n")
        player_info = {}

        player_1 = Player(name_1, 0)
        player_2 = Player(name_2, 0)
        player_vs_player.load_game()

        while True:
            print(f">>>> {player_1.name} vs {player_2.name} <<<<\n")

            current_player = player_1

            while current_player.get_score() < 100:
                print("*********************************")
                print(f" >>> {current_player.name}s turn <<<")
                print("*********************************")

                current_player.player_move()

                if current_player.get_score() >= 100:
                    print(colors.YELLOW + "*********************************"
                          + colors.RESET)
                    print(f"{current_player.name} wins!\n")
                    print(colors.YELLOW + "*********************************"
                          + colors.RESET)
                    return current_player.name

                if current_player == player_1:
                    print(colors.PINK + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                          + colors.RESET)
                    print(f"{current_player.name} got "
                          + f"{current_player.get_score()}AAAAAAAAAAAAAAAAAA")
                    print(colors.PINK + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                          + colors.RESET)
                    player_dict = player_info[current_player.name] = current_player.get_score()
                    player_vs_player.save_game(player_dict)
                    current_player = player_2
                else:
                    print(colors.PINK + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                          + colors.RESET)
                    print(f"{current_player.name} got "
                          + f"{current_player.get_score()}AAAAAAAAAAAAAAAAAAAAAA")
                    print(colors.PINK + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                          + colors.RESET)
                    current_player = player_1
