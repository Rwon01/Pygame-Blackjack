import pygame
from settings import *
import os


class Card(pygame.sprite.Sprite):

    card_group = pygame.sprite.Group()

    def __init__(self, position=[0,0], imageDirectory="assets/jokerSet/black_joker.png", is_hidden = False):
        super().__init__()
        self.card_group.add(self)
        self.image = pygame.image.load(imageDirectory).convert_alpha()
        self.hiddenImage = pygame.image.load("assets/card_back.png").convert_alpha()
        self.hiddenImageScaled = pygame.transform.scale(self.hiddenImage, (self.hiddenImage.get_width() * CARD_SCALE_FACTOR, self.hiddenImage.get_height() * CARD_SCALE_FACTOR))
        self.imageScaled = pygame.transform.scale(self.image, (self.image.get_width() * CARD_SCALE_FACTOR, self.image.get_height() * CARD_SCALE_FACTOR))
        self.rect = self.imageScaled.get_rect()
        self.rect.center = position
        self.is_hidden = is_hidden

    def move(self, newPos):
        self.rect.center = newPos
    
    def render(self, surface):
        if not self.is_hidden:
            surface.blit(self.imageScaled, self.rect.topleft)
        elif self.is_hidden:
            surface.blit(self.hiddenImageScaled, self.rect.center)

    