import pydealer.stack
import pygame
from Card import Card
from Blackjack import Blackjack
import time

FACE_CARDS = ['Jack', 'Queen', 'King']
MAX_VALUE = 21

class Player():

    def __init__(self, starting_position=[0,0]):
        self.starting_position = starting_position
        self.hand = pydealer.Stack()
        self.hand_value = 0
        self.has_busted = False

    def add_card(self):
        self.hand.add(Blackjack.pile.deal(1))

    def empty_hand(self):
        Blackjack.pile.add(self.hand.empty(return_cards=True))

    def get_hand_value(self):
        runningTotal = 0
        num_aces = 0
        for card in self.hand:
            if card.value in FACE_CARDS:
                runningTotal += 10
            elif card.value == 'Ace':
                num_aces += 1
                runningTotal += 11  # Initially, we assume Ace has a value of 11
            else:
                runningTotal += int(card.value)

        # Adjust the value of Aces if the total exceeds 21
        while runningTotal > MAX_VALUE and num_aces > 0:
            runningTotal -= 10
            num_aces -= 1

        self.hand_value = runningTotal
        return runningTotal
    



