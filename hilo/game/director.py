from Card.card import Card
#import random

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card: The current card
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """

        self.card = Card()
        self.is_playing = True
        self.total_score = 300
        self.guess =''


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
        """Ask the user if they want to select higher or 
        lower based off the first card.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        print(f'The card is: {self.card.card_1}')
        self.guess = input("Higher or lower? [h/l] ")

  
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 
    
        if self.guess == 'h':
            self.card.high()
        
        if self.guess == 'l':
            self.card.low()

        self.total_score += self.card.points
        

    def do_outputs(self):
        """Displays the new card and the score. Also asks the player if they want to play again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        
        #self.card.rotation()
        print(f"Next card was: {self.card.card_2}")
        print(f"Your score is: {self.total_score}\n")
        self.card.show_card()
        
        self.is_playing = (self.total_score > 0)

        if not self.is_playing:
            return

        new_round = input('Play again? [y/n] ')
        self.is_playing = (new_round == 'y')