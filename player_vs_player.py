"""Player vs Player class."""
from Player import Player
from colors import colors


class player_vs_player:
    """This is a class for a player vs player game."""

    def __init__(self):
        """Initialize the player vs player game."""
        self.loser = ""
        self.winner = ""

    def two_player_game(self, name_1, name_2):
        """Simulate a two player game of Pig."""
        print(">> Welcome to a game of Pig! <<\n")

        player_1 = Player(name_1, 0)
        player_2 = Player(name_2, 0)

        while True:
            print(f">>>> {player_1.name} vs {player_2.name} <<<<\n")

            current_player = player_1

            while current_player.get_score() < 100:
                print("*********************************")
                print(f" >>> {current_player.name}s turn <<<")
                print("*********************************")

                current_player.player_move()

                if current_player.get_score() >= 100 and current_player.get_score() != 200:
                    print(colors.YELLOW + "*********************************"
                          + colors.RESET)
                    print(f"{current_player.name} wins!\n")
                    print(colors.YELLOW + "*********************************"
                          + colors.RESET)
                    if current_player == player_1:
                        self.loser = player_2.name

                    elif current_player == player_2:
                        self.loser = player_1.name

                    self.winner = current_player.name

                    return current_player.name

                if current_player.get_score() >= 200:
                    self.score = 0
                    self.name = ""
                    return

                if current_player == player_1:
                    print(colors.PINK + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                          + colors.RESET)
                    print(f"{current_player.name} got "
                          + f"{current_player.get_score()}")
                    print(colors.PINK + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                          + colors.RESET)
                    current_player = player_2
                else:
                    print(colors.PINK + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                          + colors.RESET)
                    print(f"{current_player.name} got "
                          + f"{current_player.get_score()}")
                    print(colors.PINK + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                          + colors.RESET)
                    current_player = player_1

    def get_winner(self):
        """Get the winner."""
        return self.winner

    def get_loser(self):
        """Get the loser."""
        return self.loser
