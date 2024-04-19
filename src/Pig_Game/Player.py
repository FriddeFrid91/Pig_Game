from Dice import Dice
from colors import colors


class Player:
    def __init__(self, name, score): 
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
            round_score += roll
            current_score = round_score + self.score
            print(f"{self.name} rolled a {roll}.\n")
            if current_score >= 100:
                self.add_score(current_score)
                print(colors.YELLOW + "*******************************" + colors.RESET)
                print(f"{self.name} wins!\n")
                print(colors.YELLOW + "*******************************" + colors.RESET)
                return self.get_score()

            if roll == 1:
                print("Oink, oink! You lost all your points for this round!\n")
                tot = current_score - round_score
                self.deduct_score(tot)
                break

            if roll > 1:
                print(colors.YELLOW + "*******************************" + colors.RESET)
                print(f"{self.name} round score: {round_score}. ")
                print(f"{self.name} total score: {current_score}. ")
                print(colors.YELLOW + "*******************************" + colors.RESET)

                while True:
                    decision = input("Roll again? (yes/no/quit): ").lower()
                    if decision in ["yes", "no", "cheat", "quit"]:
                        break
                    print("Invalid input. Please enter yes, no, or quit.")

                if decision.lower() == "no":
                    print(colors.YELLOW + "***************************" + colors.RESET)
                    print(f"{self.name} round score: {round_score}. ")
                    print(f"{self.name} total score: {current_score}. ")
                    print(colors.YELLOW + "***************************" + colors.RESET)
                    self.add_score(round_score)
                    break
                elif decision.lower() == "yes":
                    continue
                elif decision.lower() == "cheat":
                    print("You are a cheater!")
                    self.add_score(100)
                    break
                elif decision.lower() == "quit":
                    self.add_score(200)
                    print(f"{self.name} has quit the game.")
                    return
                else:
                    print("Invalid input. Please enter yes or no.\n")

    def get_name(self):
        """Get the name of the player."""
        return self.name

    def get_score(self):
        """Get the score of the player."""
        return self.score

    def add_score(self, score):
        """Add the score of the player."""
        self.score += score

    def set_score(self, score):
        """Set the score of the player."""
        self.score = score

    def deduct_score(self, score):
        """Deduct the score of the player."""
        self.score = score
        if self.score < 0:
            self.score = 0
        return self.score
