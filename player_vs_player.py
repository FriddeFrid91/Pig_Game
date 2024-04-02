"""Player vs Player class."""
from Player import Player
from colors import colors


class player_vs_player:
    """This is a class for a player vs player game."""
    def __init__(self):
        """Initialize the player vs player game."""
        self.player_1 = Player("")
        self.player2 = Player("")

    def two_player_game(self):
        """Simulate a two player game of Pig."""
        print(">> Welcome to a game of Pig! <<")

        self.player_1 = input("Enter the name of player 1: ")
        self.player_2 = input("Enter the name of player 2: ")

        player_1 = Player(self.player_1, 0)
        player_2 = Player(self.player_2, 0)

        while True:
            print(f">>>> {player_1.name} vs {player_2.name} <<<<\n")

            current_player = player_1

            while current_player.get_score() < 50:
                print("*********************************")
                print(f"* {current_player.name}'s turn:".center(20))
                print("*********************************")

                current_player.player_move()

                if current_player.get_score() >= 50:
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
                          + {current_player.get_score()})
                    print(colors.PINK + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                          + colors.RESET)
                    current_player = player_2
                else:
                    print(colors.PINK + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                          + colors.RESET)
                    print(f"{current_player.name} got "
                          + {current_player.get_score()})
                    print(colors.PINK + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                          + colors.RESET)
                    current_player = player_1
