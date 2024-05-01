import pygame
from Card import Card
from settings import *

class Button(pygame.sprite.Sprite):

    button_group = pygame.sprite.Group()
    def __init__(self, position=[0,0], imageDirectory="assets/buttonsSet/button1.png", text = "NULL", text_size = 24):
        super().__init__()
        self.button_group.add(self)
        self.text = text
        self.image = pygame.image.load(imageDirectory).convert_alpha()
        self.imageScaled = pygame.transform.scale(self.image, (self.image.get_width() * BUTTON_SCALE_FACTOR, self.image.get_height() * BUTTON_SCALE_FACTOR))
        self.rect = self.imageScaled.get_rect()
        self.rect.center = position
        self.text_font = pygame.font.SysFont("Arial Black", text_size)
        self.textFont = self.text_font.render(self.text, True, "Black")
        self.clicked = False

    def move(self, newPos):
        self.rect.center = newPos
    
    def is_clicked(self):

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
        surface.blit(self.imageScaled, self.rect.topleft)
        surface.blit(self.textFont, [self.rect.centerx - self.textFont.get_width()//2, self.rect.centery - self.textFont.get_height()//2])
        


