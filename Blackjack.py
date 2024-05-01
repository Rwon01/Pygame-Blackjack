import pydealer.stack
import pygame
from settings import *


class Blackjack():
    
    amount_of_decks = AMOUNT_OF_DECKS
    #Create deck pile
    pile = pydealer.Stack()
    single_deck = pydealer.Deck()
    discard_pile = pydealer.Stack()
    for i in range(amount_of_decks):
        pile.add(single_deck)
        pile.shuffle()   

    def __init__(self):
        pass  
    
    def play_round():
        pass
