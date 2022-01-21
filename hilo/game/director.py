import random
from game.hilo import Hilo

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def _init_(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """

        """ """
        self.hilo = random.randint(1,13)
        self.is_playing =True
        self.choose_1 =0
        self.choose_2 =0
        self.score = 300
        self.total_score = 0
        self.high_lower =""

       

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """

        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        
        
        """
        choose_1 = random.randint(1,13)
        print(f"The card is: {choose_1} ")
        self.high_lower = input("Higher or Lower? [h/l]:  ")

        choose_2 = random.randint(1,13)
        print(f"Next card was: {choose_2} ")
            """
        self.high_lower = input("Higher or Lower? [h/l]:  ")
        self.high_lower = input("Higher or Lower? [h/l]:  ")  
        self.is_playing = input("Play again [y/n]: ")

       
       
            
    def do_updates(self):
        """Updates the player's score.
        
        Args:
            self (Director): An instance of Director.
        """
        self.choose_2 = random.randint(1,13)
        self.choose_2 = random.randint(1,13)
        if self.high_lower == "h":
            if self.choose_1 < self.choose_2:   
                self.total_score = self.score + 100
            else:
                self.total_score = self.score - 75     
        elif self.high_lower == "l":      
            if self.choose_1 > self.choose_2:   
                self.total_score = self.score + 100
            else:
                self.total_score = self.score - 75   

        

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        print(f"Your score is: {self.total_score}")
        if self.total_score == 0:
            print("Game Over")
        
#        play_again=input("Play again [y/n]: ")
        if self.is_playing =="y":
            #play()
            input()
            
        
        if self.is_playing =="n":
            print("Thank you for playing!")
        