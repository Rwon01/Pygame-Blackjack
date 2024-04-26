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



run = True
while run:

    clock.tick(FPS)

    #COLLISION CHECK
    mousePos = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0] == 1:
        if btnDeal.rect.collidepoint(mousePos):
            btnDeal.move( [mousePos[0] - btnDeal.rect.w // 2, mousePos[1] - btnDeal.rect.h // 2])
        if cardtest.rect.collidepoint(mousePos):
            cardtest.move( [mousePos[0] - cardtest.rect.w // 2, mousePos[1] - cardtest.rect.h // 2])

    screen.fill("dark gray")
    
    
    for button in buttonGroup:
        button.render(screen)

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
            


pygame.quit()