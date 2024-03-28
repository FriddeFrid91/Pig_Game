"""Player vs Player class."""
from Player import Player


class playervsplayer:
    def __init__(self):
        self.Player1 = Player("")
        self.Player2 = Player("")

    def total_rounds():
        pass

    def round_score():
        pass

    def total_score():
        pass
             
    def two_player_game(self):
        print(">> Welcome to a game of Pig! <<")

        self.Player1 = input("Enter the name of player 1: ")
        self.Player2 = input("Enter the name of player 2: ")

        player1 = Player(self.Player1, 0)
        player2 = Player(self.Player2, 0)

        while True:
            print(f">> {player1.name} vs {player2.name} <<\n")

            current_player = player1

            while current_player.get_score() < 100:
                print(f"{current_player.name}'s turn:\n")
                current_player.player_move()

                if current_player.get_score() >= 100:
                    print(f"{current_player.name} wins!\n")
                    break

                if current_player == player1:
                    current_player = player2
                else:
                    current_player = player1











