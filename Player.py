class Player:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score
        self.dice = self.dice(6)

    def __str__(self):
        return f"{self.name} has {self.score} points."

    def player_move(self):
        """Simulate a player's move."""
        round_score = 0
        while True:
            tot_score = self.get_score()
            roll = self.dice.roll_the_dice()
            print(f"{self.name} rolled a {roll}.")
            if roll == 1:
                print(f"{self.name} rolled a 1. You get 0 points from this round.")
                print(f"{self.name} total score: {tot_score}.")
                break
            round_score += roll
            print(f"{self.name} round score: {round_score}.")
            decision = input("Roll again? (y/n): ")
            if decision != "y":
                break
            self.add_score(round_score)
            print(tot_score)
    
    def add_to_the_score(self, score):
        """Add to the score of the player."""
        self.score += score

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
