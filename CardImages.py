import pygame
import os
import random
from settings import *
from Card import Card
import pydealer

CARDS_PATH = list()

class CardImages():

    def __init__(self):
        pass

    def getCardFiles(self):
        for path in os.listdir('assets\cardsSet'):
            cardpath = "assets/cardsSet/" + path
            CARDS_PATH.append(cardpath)

        return CARDS_PATH

            
