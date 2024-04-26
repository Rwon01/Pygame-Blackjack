import pygame
from Card import Card
from settings import *

class Button(pygame.sprite.Sprite):
    


    def __init__(self, position=[SCREEN_WIDTH//2,SCREEN_HEIGHT//2], imageDirectory="assets/buttonsSet/button1.png", text = "NULL"):
        super().__init__()
        self.position = position
        self.image = pygame.image.load(imageDirectory).convert_alpha()
        self.imageScaled = pygame.transform.scale(self.image, (self.image.get_width() * BUTTON_SCALE_FACTOR, self.image.get_height() * BUTTON_SCALE_FACTOR))
        self.rect = self.imageScaled.get_rect(x = self.position[0], y = self.position[1])
        text_font = pygame.font.SysFont("Arial Black", 24)
        self.textFont = text_font.render(text, True, "Black")

    def move(self, newPos):
        self.position = newPos
        self.rect.topleft = self.position
        
    
    def getPos(self):
        return self.position

    def render(self, surface):
        surface.blit(self.imageScaled, self.position)
        surface.blit(self.textFont, self.position)
        


