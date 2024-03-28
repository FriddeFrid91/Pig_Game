"""class for the game Rules"""

class colors:
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        BLUE = '\033[94m'
        PINK = '\033[95m'
        RESET = '\033[0m'  

class Rules:
    def __init__(self): #constructor
        self.rules = "You can play the game with 1 players with the computer\nYou can play the game with 2 players\nFirst player to get 100 points wins\nIf you roll a 1,you lose all your points for that turn\nIf you hold, you keep your points for that turn"
        print(colors.PINK + "**RULES OF PIG GAME**" + colors.RESET) #prints the rules of the game
        print(colors.YELLOW + "*******************************************************" + colors.RESET)
        print(colors.BLUE + "You can play the game with 1 player with the computer" + colors.RESET)
        print(colors.BLUE + "You can play the game with 2 players" + colors.RESET)
        print(colors.BLUE + "First player to get 100 points wins" + colors.RESET)
        print(colors.GREEN + "If you roll a 1, you lose all your points for that turn" + colors.RESET)
        print(colors.BLUE + "If you hold, you keep your points for that turn" + colors.RESET)
        print(colors.YELLOW + "*******************************************************" + colors.RESET)

    def get_rules(self): #returns the rules
        return self.rules 