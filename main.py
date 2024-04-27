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
#CREATE BUTTON
btnHit = Button(text="HIT")
btnStand = Button(text="STAND")
btnDouble = Button(text="DOUBLE")
btnSplit = Button(text="SPLIT")
btnSurrender = Button(text="SURRENDER", text_size=18)

cardtest = Card()

#GUI CONST
POS_X = SCREEN_WIDTH * 0.50 - btnDouble.rect.w // 2
rect_size = btnDouble.rect.w
#GUI
btnHit.move([POS_X - 2 * rect_size , SCREEN_HEIGHT - 200])
btnStand.move([POS_X - 1 * rect_size, SCREEN_HEIGHT - 200])
btnDouble.move([POS_X, SCREEN_HEIGHT - 200])
btnSplit.move([POS_X + 1 * rect_size, SCREEN_HEIGHT - 200])
btnSurrender.move([POS_X + 2* rect_size, SCREEN_HEIGHT - 200])

buttonGroup = pygame.sprite.Group()
buttonGroup.add(btnStand)
buttonGroup.add(btnHit)
buttonGroup.add(btnDouble)
buttonGroup.add(btnSplit)
buttonGroup.add(btnSurrender)
#buttonGroup.add(cardtest)


#GAMELOOP
run = True
while run:

    clock.tick(FPS)

    #COLLISION CHECK
    mousePos = pygame.mouse.get_pos()





    #BACKGROUND
    screen.fill("dark gray")
    
    #RENDER ENTITIES
    for button in buttonGroup:
        button.onClick()
        button.render(screen)

    #UPDATE DISPLAY -- KEEP LAST
    pygame.display.flip()


    #EXIT GAME
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
            


pygame.quit()