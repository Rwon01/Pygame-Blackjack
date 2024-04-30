import pydealer.stack
import pygame
import pydealer
from Player import Player


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
    
def play_round():
    pass