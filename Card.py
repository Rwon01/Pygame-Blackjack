import pygame
from settings import *
import os

class Card(pygame.sprite.Sprite):
    
    def __init__(self, position=[SCREEN_WIDTH//2,SCREEN_HEIGHT//2], imageDirectory="assets/jokerSet/black_joker.png", cardValue = 0):
        super().__init__()
        self.cardValue = cardValue
        self.position = position
        self.image = pygame.image.load(imageDirectory).convert_alpha()
        self.hiddenImage = pygame.image.load("assets/card_back.png").convert_alpha()
        self.hiddenImageScaled = pygame.transform.scale(self.hiddenImage, (self.hiddenImage.get_width() * CARD_SCALE_FACTOR, self.hiddenImage.get_height() * CARD_SCALE_FACTOR))
        self.imageScaled = pygame.transform.scale(self.image, (self.image.get_width() * CARD_SCALE_FACTOR, self.image.get_height() * CARD_SCALE_FACTOR))
        self.rect = self.imageScaled.get_rect(x = self.position[0], y = self.position[1])
        self.isHidden = False

    def move(self, newPos):
        self.position = newPos
        self.rect.topleft = self.position
    
    def getPos(self):
        return self.position

    def render(self, surface):
        if not self.isHidden:
            surface.blit(self.imageScaled, self.position)
        elif self.isHidden:
            surface.blit(self.hiddenImageScaled, self.position)

    