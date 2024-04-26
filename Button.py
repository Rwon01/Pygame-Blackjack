import pygame
from Card import Card
from settings import *

class Button(pygame.sprite.Sprite):

    def __init__(self, position=[0,0], imageDirectory="assets/buttonsSet/button1.png", text = "NULL", text_size = 24):
        super().__init__()
        self.position = position
        self.image = pygame.image.load(imageDirectory).convert_alpha()
        self.imageScaled = pygame.transform.scale(self.image, (self.image.get_width() * BUTTON_SCALE_FACTOR, self.image.get_height() * BUTTON_SCALE_FACTOR))
        self.rect = self.imageScaled.get_rect(center=position)
        text_font = pygame.font.SysFont("Arial Black", text_size)
        self.textFont = text_font.render(text, True, "Black")

    def move(self, newPos):
        self.position = newPos
        self.rect.center = newPos
        
    
    def getPos(self):
        return self.position

    def render(self, surface):
        surface.blit(self.imageScaled, self.position)
        surface.blit(self.textFont, [self.position[0] + 30, self.position[1] + 45])
        


