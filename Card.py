import pygame
from settings import *
import os

class Card(pygame.sprite.Sprite):
    
    def __init__(self, position=[SCREEN_WIDTH//2,SCREEN_HEIGHT//2], imageDirectory="assets/jokerSet/black_joker.png", cardValue = 0):
        super().__init__()
        self.cardValue = cardValue
        self.position = position
        self.image = pygame.image.load(imageDirectory).convert_alpha()
        self.imageScaled = pygame.transform.scale(self.image, (self.image.get_width() * CARD_SCALE_FACTOR, self.image.get_height() * CARD_SCALE_FACTOR))
        self.rect = self.imageScaled.get_rect(x = self.position[0], y = self.position[1])

    def move(self, newPos):
        self.position = newPos
        self.rect.topleft = self.position
    
    def getPos(self):
        return self.position

    def render(self, surface):
        surface.blit(self.imageScaled, self.position)

    