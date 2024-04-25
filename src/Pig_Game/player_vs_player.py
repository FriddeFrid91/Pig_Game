"""Player vs Player class."""
from Player import Player
from colors import colors


class player_vs_player:
    """This is a class for a player vs player game."""

    def __init__(self):
        """Initialize the player vs player game."""
        self.loser = ""
        self.winner = ""
        self.score = 0
        self.name = ""

    def set_loser(self, loser):
        """Set the loser."""
        self.loser = loser

    def set_winner(self, winner):
        """Set the winner."""
        self.winner = winner

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
                # If the current player gets a 100 points, they win.
                if current_player.get_score() >= 100 and current_player.get_score() != 200:
                    if current_player == player_1:
                        self.loser = player_2.name
                        self.set_loser(player_2.name)

                    elif current_player == player_2:
                        self.loser = player_1.name
                        self.set_loser(player_1.name)

                    self.set_winner(current_player.name)
                    self.get_winner()

                    return current_player.name
                # Not an elegant solution, but it works. If the current player
                # wants to quit the game, they can type "quit"
                # and the game will end.
                # But they get 200 points so this if statements works.
                # And returns no one as the winner.
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

    def get_loser(self):
        """Get the loser."""
        return self.loser

    def get_winner(self):
        """Get the winner."""
        return self.winner
