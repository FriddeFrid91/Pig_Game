#a class for the game Rules

class Rules:
    def __init__(self): #constructor
        self.rules = "You can play the game with 1 players with the computer\nYou can play the game with 2 players\nFirst player to get 100 points wins\nIf you roll a 1, you lose all your points for that turn\nIf you hold, you keep your points for that turn"
        print("Rules of the game") #prints the rules of the game
        print("You can play the game with 1 player with the computer")
        print("You can play the game with 2 players")
        print("First player to get 100 points wins")
        print("If you roll a 1, you lose all your points for that turn")
        print("If you hold, you keep your points for that turn")

    def get_rules(self): #returns the rules
        return self.rules 
    
