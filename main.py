import pygame
import random
import os
from Card import Card
from settings import *
from CardImages import CardImages
from Button import Button

#BOILERPLATE FOR PYGAME
pygame.init()

os.environ['SDL_VIDEO_CENTER'] = '1'
info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT - 50), pygame.RESIZABLE)
pygame.display.set_caption("Blackjack Game")
clock = pygame.time.Clock()

#CREATE INSTANCES 
d = CardImages()
btnHit = Button(text="HIT")
btnDeal = Button(text="DEAL")
cardtest = Card()

#GUI
btnHit.move([200, 100])
btnDeal.move([200, 150])
buttonGroup = pygame.sprite.Group()
buttonGroup.add(btnHit)
buttonGroup.add(btnDeal)
buttonGroup.add(cardtest)


#GAMELOOP
run = True
while run:

    clock.tick(FPS)

    #COLLISION CHECK
    mousePos = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0] == 1:
        if btnDeal.rect.collidepoint(mousePos):
            btnDeal.move([0,0])



    #BACKGROUND
    screen.fill("dark gray")
    
    #RENDER ENTITIES
    for button in buttonGroup:
        button.render(screen)

    #UPDATE DISPLAY -- KEEP LAST
    pygame.display.flip()


    #EXIT GAME
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
            


pygame.quit()