from Player import Player
from Card import Card

class Dealer(Player):

    def __init__(self, starting_position):
        super().__init__()
        self.starting_position = starting_position
        self.hidden_card = True

    def reveal_card(self):
        self.hidden_card = False
        pass