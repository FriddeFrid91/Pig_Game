import random


class Computer:
    """Class represennting a computer player."""
    def __init__(self):
        """Initialize the computer player."""
        self.name = "Computer"
        self.score = 0

    def computer_move(self):
        """Simulate the computer's move."""
        roll = random.randint(1, 6)
        if roll == 1:
            print("Oink, oink! The computer lost all its points for this round!\n")
        else:
            print(f"The computer rolled a {roll}.\n")
            self.score += roll
