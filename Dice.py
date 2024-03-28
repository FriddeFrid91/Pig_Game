import random
"""Module for the dice."""


class Dice:
    """Class for the dice."""
    def __init__(self, numbers):  # Constructor
        # roll_the_dice = 0  # Variable to store the result of the dice roll
        self.numbers = numbers  # Number of sides of the dice

    def roll_the_dice(self):  # Method to roll the dice
        """Roll the dice."""
        return random.randint(1, self.numbers)
    # Return a random number between 1 and the number of sides of the dice

    def showTheDice(self, result, listOfPoints):  # Method to show the dice
        """Show the dice."""
        if result == 1:
            # If the result is 1, the player loses all the points and the turn is over
            print("--------------------")
            print("Sorry, you got a 1. Your turn is over.")
            print("--------------------")
            listOfPoints.clear()  # Clear the list of points
            return 0
        else:
            # If the result is not 1, the player gets
            # the points and can continue playing
            print(f"You got a {result}!")
            return result

    def getDice(self):  # Getter
        """Get the dice."""
        return self.numbers

    def setDice(self, numbers):  # Setter
        """Set the dice."""
        self.numbers = numbers

    def __str__(self):
        """Print the dice."""
        # Method to print the dice
        return f"The dice has {self.numbers} sides."
    # Return the number of sides of the dice
