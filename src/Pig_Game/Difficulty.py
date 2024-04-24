"""Class for difficulty."""
import random


class Difficulty:
    """Class for difficulty."""

    def __init__(self, difficulty):
        """Initialize the difficulty."""
        self.difficulty = difficulty
        self.difficulty = 0

        Difficulty = input("Enter the difficulty: Easy, Medium or Hard?: \n")

        if Difficulty[0].upper() == "E":
            d = random.randint(1, 10)
        elif Difficulty[0].upper() == "M":
            d = random.randint(1, 50)
        elif Difficulty[0].upper() == "H":
            d = random.randint(1, 100)
        else:
            raise Exception("Invalid input, please type a difficulty: \n")
        self.difficulty = d
        print(f"Difficulty is set to {d}.")

    def get_difficulty(self):
        """Get the difficulty."""
        return self.difficulty

    def set_difficulty(self, difficulty):
        """Set the difficulty."""
        self.difficulty = difficulty

if __name__ == "__main__":
    difficulty = Difficulty()
    print(difficulty.get_difficulty())
    difficulty.set_difficulty(50)
    print(difficulty.get_difficulty())
    difficulty.set_difficulty(100)
    print(difficulty.get_difficulty())
    difficulty.set_difficulty(10)
    print(difficulty.get_difficulty())