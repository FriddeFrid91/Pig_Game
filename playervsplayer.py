"""Player vs Player class."""
from Player import Player


class playervsplayer:
    def __init__(self):
        self.Player1 = Player("")
        self.Player2 = Player("")

    def two_player_game(self):
        print(">> Welcome to a game of Pig! <<")

        self.Player1 = input("Enter the name of player 1: ")
        self.Player2 = input("Enter the name of player 2: ")

        player_1 = Player(self.Player1, 0)
        player_2 = Player(self.Player2, 0)

        while True:
            print(f">> {player_1.name} vs {player_2.name} <<\n")

            current_player = player_1

            while current_player.get_score() < 50:
                print("*********************************")
                print(f"* {current_player.name}'s turn: *\n")
                print("**********************************")
                current_player.player_move()

                if current_player.get_score() >= 50:
                    print(f"{current_player.name} wins!\n")
                    return current_player.name

                if current_player == player_1:
                    print(current_player.get_score())
                    print(f"{current_player.name} got  {current_player.get_score()}")
                    current_player = player_2
                else:
                    print(f"{current_player.name} got  {current_player.get_score()}")
                    current_player = player_1











