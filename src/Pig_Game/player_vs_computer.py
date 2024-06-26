"""Player vs Computer class."""
from Player import Player
from Computer import Computer
from colors import colors


class player_vs_computer:
    """This is a class for a player vs computer game."""

    def __init__(self):
        """Initialize the player vs computer game."""
        self.player = Player("", 0)
        self.computer = Computer()

    def player_vs_computer_game(self, difficulty):
        """Simulate a player vs computer game of pig."""
        print(colors.YELLOW + colors.TextStyles.ITALIC + ">> Welcome to a game of Pig! <<\n" + colors.RESET)
        self.computer.set_difficulty(difficulty)

        while True: 
            self.player.name = input(colors.PINK + "Enter your name: " + colors.RESET)
            if self.player.name:
                break
            else:
                print(colors.PINK + "Please enter a name.\n" + colors.RESET)

     

        while True: 
            print(colors.BLUE + f">>>> {self.player.name} vs computer <<<<\n" + colors.RESET)


            current_player = self.player

            while current_player.get_score() < 100:
                print("*********************************")
                print(f" >>> {current_player.name}s turn <<<")
                print("*********************************")

                if current_player == self.player:
                    current_player.player_move()
                else:
                    current_player = self.computer
                    self.computer.computer_move()

                if current_player.get_score() >= 100:
                    print(colors.YELLOW + "*********************************" + colors.RESET)
                    print(f"{current_player.name} wins!\n")
                    print(colors.YELLOW + "*********************************" + colors.RESET)
                    return current_player.name

                if current_player == self.player:
                    print(colors.PINK + "*********************************" + colors.RESET)
                    print(f"{current_player.name} got {current_player.get_score()}")
                    print(colors.PINK + "*********************************" + colors.RESET)
                    current_player = self.computer
                    continue
                else:
                    print(colors.PINK + "*********************************" + colors.RESET)
                    print("Computer's score: ", current_player.get_score())
                    print(colors.PINK + "*********************************" + colors.RESET)
                    current_player = self.player
                    continue
            break
