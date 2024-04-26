import pygame
import random
from Card import Card
from settings import *
from CardImages import CardImages
from Button import Button

#BOILERPLATE FOR PYGAME
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Blackjack Game")
clock = pygame.time.Clock()

#CREATE BUTTONS AND GROUPS
d = CardImages()
btn1 = Button(text="HIT").move([200, 100])
btn2 = Button(text="HIT").move([200, 150])
buttonGroup = pygame.sprite.Group().add(btn1, btn2)

run = True
while run:

    clock.tick(FPS)

    #COLLISION CHECK
    mousePos = pygame.mouse.get_pos()
    if btn1.rect.collidepoint(mousePos):
        if pygame.mouse.get_pressed()[0] == 1:
            pass
    

    screen.fill("dark gray")
    

    for button in buttonGroup:
        button.render(screen)
    
    pygame.display.flip()


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
            


pygame.quit()