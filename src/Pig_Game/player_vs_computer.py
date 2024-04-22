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
        print(">> Welcome to a game of Pig! <<\n")
        self.computer.set_difficulty(difficulty)




        while True:
            self.player.name = input("Enter your name: ")
            if self.player.name:
                break
            else:
                print("Please enter a name.\n")
                
        with open("player.txt", "w") as f:
            f.write(self.player.name)

        while True:
            print(f">>>> {self.player.name} vs computer <<<<\n")

            current_player = self.player

            while current_player.get_score() < 50:
                print("*********************************")
                print(f" >>> {current_player.name}s turn <<<")
                print("*********************************")

                if current_player == self.player:
                    current_player.player_move()
                else:
                    self.computer.computer_move()
                    current_player = self.computer

                if current_player.get_score() >= 50:
                    print(colors.YELLOW + "*********************************")
                    print(f"{current_player.name} wins!\n")
                    print(colors.YELLOW + "*********************************")
                    return current_player.name

                if current_player == self.player:
                    print(colors.PINK + "*********************************")
                    print(f"{current_player.name} got {current_player.get_score()}")
                    print(colors.PINK + "*********************************")
                    current_player = self.computer
                else:
                    print(colors.PINK + "*********************************")
                    print("Computer's score: ", current_player.get_score())
                    print(colors.PINK + "*********************************")
                    current_player = self.player
