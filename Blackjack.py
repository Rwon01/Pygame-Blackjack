import pydealer.stack
import pygame
import pydealer

MAX_VALUE = 21
FACE_CARDS = ['Jack', 'Queen', 'King']


class Blackjack():

# DeckSize, 
    
    def __init__(self, amount_of_decks):
        self.amount_of_decks = amount_of_decks

        #Create deck pile
        self.pile = pydealer.Stack()
        single_deck = pydealer.Deck()
        self.discard_pile = pydealer.Stack()
        for i in range(self.amount_of_decks):
            self.pile.add(single_deck)
            self.pile.shuffle()
        
    def dealCard(self, amount):
        return self.pile.deal(amount)
    
    def getHandTotal(self, hand):
        runningTotal = 0
        num_aces = 0
        for card in hand:
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

        return runningTotal