from Player import Player
from Dealer import Dealer
from Blackjack import Blackjack
from settings import *

class Game:

    def __init__(self):
        self.deck = Blackjack.pile
        self.dealer = Dealer(starting_position=[SCREEN_WIDTH*0.25, 150])
        self.player = Player(starting_position=[SCREEN_WIDTH*0.25, 500])

    def hit(self):
        if self.player.get_hand_value() <= 21:
            self.player.add_card()

    def stand(self):
        pass

    def deal_round(self):
        self.player.add_card()
        self.player.add_card()
        self.dealer.add_card()
        self.dealer.add_card()

