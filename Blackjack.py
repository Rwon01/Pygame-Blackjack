import pygame
import pydealer

class Blackjack():

# DeckSize, 

    def __init__(self, amount_of_decks):
        self.amount_of_decks = amount_of_decks

        #Create deck pile
        self.pile = pydealer.Stack()
        single_deck = pydealer.Deck()
        for i in range(self.amount_of_decks):
            self.pile.add(single_deck)

    def dealCard(self, amount):
        return self.pile.deal(amount)
    
    def getHandTotal(self, hand):
        pass