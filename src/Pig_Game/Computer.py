"""This module contains the Computer class."""
import random
from Dice import Dice
from colors import colors


class Computer:
    """Class represennting a computer player."""
    def __init__(self):
        """Initialize the computer player."""
        self.name = "Computer"
        self.score = 0
        self.difficulty = None
        self.Dice = Dice(6)

    def set_difficulty(self, difficulty):
        """Set the difficulty level of the computer."""
        self.difficulty = difficulty

    def get_score(self):
        """Return the computer's score."""
        return self.score

    def computer_move(self):
        """Simulate the computer's move."""
        if self.difficulty == "easy":
            self.easy_difficulty()
        elif self.difficulty == "medium":
            self.medium_difficulty()
        elif self.difficulty == "hard":
            self.hard_difficulty()
        else:
            raise ValueError("Invalid difficulty level.")

    def easy_difficulty(self):
        """Set the difficulty to easy."""
        roll = self.Dice.roll_the_dice()

        counting_round = 0
        boolean = True
        while boolean:
            if counting_round == 3:
                print(colors.BLUE + "The computer has decided to hold.\n"
                      + colors.RESET)
                print(colors.GREEN + f"The computer's score is {self.score}.\n"
                      + colors.RESET)
                boolean = False
                break
            if roll == 1:
                print(colors.RED + "Oink, oink! The computer lost all its " +
                      "points for this round!\n" + colors.RESET)
                boolean = False
                break
            elif roll == 6:
                print(colors.BLUE + "The computer has decided to hold.\n"
                      + colors.RESET)
                print(colors.GREEN + f"The computer's score is {self.score}.\n"
                      + colors.RESET)
                boolean = False
                break
            else:
                print(colors.CYAN + f"The computer rolled a {roll}.\n"
                      + colors.RESET)
                self.score += roll
                print(colors.GREEN + f"The computer's score is {self.score}.\n"
                      + colors.RESET)
                counting_round += 1

    def medium_difficulty(self):
        """Set the difficulty to medium."""
        roll = random.randint(1, 10)
        if roll == 1:
            print("Oink, oink! The computer cheatycheats, "
                  + "and not lose any point HAHAHA!\n")

        else:
            print(f"The computer rolled a {roll}.\n")
            self.score += roll
            if self.score >= 10:
                print("The computer has decided to hold.\n")
                print(f"The computer's score is {self.score}.\n")

    def hard_difficulty(self):
        """Set the difficulty to hard."""
        roll = random.randint(4, 10)
        if roll == 1:
            print("Oink, oink! NO ones for me \n")        
        else:
            print(f"The computer rolled a {roll}.\n")
            self.score += roll
            if self.score >= 20:
                print("The computer has decided to hold.\n")
                print(f"The computer's score is {self.score}.\n")
