from Dice import Dice


class Player:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score
        self.dice = Dice(6)

    def __str__(self):
        return f"{self.name} has {self.score} points."

    def player_move(self):
        """Simulate a player's move."""
        round_score = 0
        while True:

            roll = self.dice.roll_the_dice()
            print(f"{self.name} rolled a {roll}.")
            if roll == 1:
                print("Oink, oink! You lost all your points for this round!\n")
                self.deduct_score(round_score)
                current_score = self.score
                break
            round_score += roll
            current_score = round_score + self.score
            print("*********************************************")
            print(f"* {self.name} round score: {round_score}. \n")

            print(f"* {self.name} total score: {current_score}. \n")
            print("*********************************************")
            decision = input("Roll again? (y/n): ")
            if decision != "y":
                print(self.get_score())
                print(f"{self.name} total score: {self.score}.\n")
                self.add_score(round_score)

                break

    def change_name(self, name):
        """Change the name of the player."""
        self.name = name

    def get_name(self):
        """Get the name of the player."""
        return self.name

    def get_score(self):
        """Get the score of the player."""
        return self.score

    def set_score(self, score):
        """Set the score of the player."""
        self.score = score

    def add_score(self, score):
        """Add the score of the player."""
        self.score += score

    def deduct_score(self, score):
        """Deduct the score of the player."""
        self.score -= score
        if self.score < 0:
            self.score = 0
        return self.score
