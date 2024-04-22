import random


class Computer:
    """Class represennting a computer player."""
    def __init__(self):
        """Initialize the computer player."""
        self.name = "Computer"
        self.score = 0
        self.difficulty = None

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
        for _ in range(2):
            roll = random.randint(1, 6)
       
        if roll == 1:
            print(f"The computer rolled a {roll}.\n")
            print("Oink, oink! The computer lost all its points for this round!\n") 
            self.score = 0
            
        
        elif roll in [3, 5]:
            print(f"The computer rolled a {roll}.\n")
            self.score += roll
            print("The computer has decided to hold.\n")

        elif roll in [15, 18]:
            print(f"The computer rolled a {roll}.\n")
            self.score += roll
            print("The computer has decided to hold.\n")
             
        else:
            print(f"The computer rolled a {roll}.\n")
            self.score += roll
            print(f"The computer's score is {self.score}.\n")
    
    def medium_difficulty(self):
        """Set the difficulty to medium."""
        for _ in range(2):  
            roll = random.randint(1, 8)
    
        if roll == 1:
                print(f"The computer rolled a {roll}.\n")
                self.score += roll
                print("Oink, oink! The computer cheatycheats, and not lose any point HAHAHA!\n")
                print(f"The computer's score is {self.score}.\n")
                self.score += roll
                

        elif 2 < roll < 6:
                print(f"The computer rolled a {roll}.\n")
                print("The computer has decided to hold.\n")
                self.score += roll
                print(f"The computer's score is {self.score}.\n")


        else:                
                print(f"The computer rolled a {roll}.\n")
                self.score += roll
                print(f"The computer's score is {self.score}.\n")
                

       

    def hard_difficulty(self):
        """Set the difficulty to hard."""
        for _ in range(2):
            roll = random.randint(4, 10)
        if roll == 1:
            print("Oink, oink! NO 1:s for me \n")   
        if roll > 7 and roll < 10:
            print (f"The computer rolled a {roll}.\n")
            print(f"The computer has decided to hold.\n")
            self.score += roll
        else:
                print(f"The computer rolled a {roll}.\n")
                self.score += roll
                if self.score >= 20:
                    print("The computer has decided to hold.\n")
                    print(f"The computer's score is {self.score}.\n")
        


    