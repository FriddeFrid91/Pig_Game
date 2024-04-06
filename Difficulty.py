"""Class for difficulty."""
import random

class Difficulty:
    """Class for difficulty."""
    def __init__(self, difficulty):
        """Initialize the difficulty."""
        self.difficulty = difficulty

Difficulty = input("Enter the difficulty: Easy, Medium or Hard?: \n")
if Difficulty[0].upper() == "E":
    d = random.randint(1, 10)
elif Difficulty[0].upper() == "M":
    d = random.randint(1, 50)
elif Difficulty[0].upper() == "H":
    d = random.randint(1, 100)
else: 
    raise Exception("Invalid input, please type a difficulty: \n")
     
