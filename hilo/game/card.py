import random 

class Card:

    def __init__(self):
        self.card_1 = random.randint(1,13)
        self.card_2 = random.randint(1,13)
        self.points = 0
    
    def show_card(self):
        self.card_1 = self.card_2
        self.card_2 = random.randint(1,13)
        return self.card_2 #This seemed to be the issue

    def low(self):
        #If player choses low
        self.points = 0
        self.points = 100 if self.card_1 > self.card_2 else -75
        
    
    def high (self):
        #If player choses high
        self.points = 0
        self.points = 100 if self.card_1 < self.card_2 else -75

      
    #def rotation (self):
        #self.card_1 = self.card_2