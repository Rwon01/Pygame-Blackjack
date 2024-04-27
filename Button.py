import pygame
from Card import Card
from settings import *

class Button(pygame.sprite.Sprite):

    def __init__(self, position=[0,0], imageDirectory="assets/buttonsSet/button1.png", text = "NULL", text_size = 24):
        super().__init__()
        self.text = text
        self.position = position
        self.image = pygame.image.load(imageDirectory).convert_alpha()
        self.imageScaled = pygame.transform.scale(self.image, (self.image.get_width() * BUTTON_SCALE_FACTOR, self.image.get_height() * BUTTON_SCALE_FACTOR))
        self.rect = self.imageScaled.get_rect(topleft=position)
        self.text_font = pygame.font.SysFont("Arial Black", text_size)
        self.textFont = self.text_font.render(self.text, True, "Black")
        self.clicked = False

    def move(self, newPos):
        self.position = newPos
        self.rect.topleft = newPos
        
    def getPos(self):
        return self.position
    
    def onClick(self):

        mousepos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mousepos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.textFont = self.text_font.render(self.text, True, "RED")
                return self.text
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            self.textFont = self.text_font.render(self.text, True, "Black")

    def render(self, surface):
        surface.blit(self.imageScaled, self.position)
        surface.blit(self.textFont, [self.position[0] + 30, self.position[1] + 45])
        


