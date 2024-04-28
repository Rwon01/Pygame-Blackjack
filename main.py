import pygame
import random
import os
from Card import Card
from settings import *
from Button import Button
from Blackjack import *


def convertToCardImage(card):
    cardpath = f"assets/cardsSet/{card.value}_of_{card.suit}.png".lower()

    card = Card(position=[random.randint(0, SCREEN_WIDTH), SCREEN_HEIGHT//2], imageDirectory=cardpath)
    return card


#BOILERPLATE FOR PYGAME
pygame.init()

os.environ['SDL_VIDEO_CENTER'] = '1'
info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT - 50), pygame.RESIZABLE)
pygame.display.set_caption("Blackjack Game")
clock = pygame.time.Clock()

#CREATE INSTANCES 
blackjack = Blackjack(AMOUNT_OF_DECKS)
playerHand = pydealer.Stack()

#CREATE BUTTON
btnHit = Button(text="HIT")
btnStand = Button(text="STAND")
btnDouble = Button(text="DOUBLE")
btnSplit = Button(text="SPLIT")
btnSurrender = Button(text="SURRENDER", text_size=18)
btnDeal = Button(text="DEAL", text_size=32)

#TEXT
remCard = pygame.font.SysFont("Arial Black", 18)


#GUI CONST
POS_X = SCREEN_WIDTH * 0.50 - btnDouble.rect.w // 2
rect_size = btnDouble.rect.w
#GUI
btnHit.move([POS_X - 2 * rect_size , SCREEN_HEIGHT - 200])
btnStand.move([POS_X - 1 * rect_size, SCREEN_HEIGHT - 200])
btnDouble.move([POS_X, SCREEN_HEIGHT - 200])
btnSplit.move([POS_X + 1 * rect_size, SCREEN_HEIGHT - 200])
btnSurrender.move([POS_X + 2* rect_size, SCREEN_HEIGHT - 200])
btnDeal.move([100, 100])

buttonGroup = pygame.sprite.Group()
cardGroup = pygame.sprite.Group()
buttonGroup.add(btnStand)
buttonGroup.add(btnHit)
buttonGroup.add(btnDouble)
buttonGroup.add(btnSplit)
buttonGroup.add(btnSurrender)
buttonGroup.add(btnDeal)



#GAMELOOP
run = True
while run:

    clock.tick(FPS)
    #COLLISION CHECK
    mousePos = pygame.mouse.get_pos()
    #BACKGROUND
    screen.fill("dark gray")
    
    #BUTTON LOOP
    for button in buttonGroup:
        test_value = button.onClick()

        if test_value == "DEAL": 
            playerHand.add(blackjack.dealCard(2))
            print(blackjack.getHandTotal(playerHand))
            
        if test_value == "HIT":
            playerHand.add(blackjack.dealCard(1))
        
        if test_value == 'STAND':
            blackjack.pile.add(playerHand.empty(return_cards=True))
            blackjack.pile.shuffle()
        if test_value == 'DOUBLE':
            for everycard in playerHand:
                d = convertToCardImage(everycard)
                cardGroup.add(d)

        button.render(screen)


    for visible_card in cardGroup:
        visible_card.render(screen)

    remainingCards = remCard.render(str(len(blackjack.pile)), True, 'Black')
    handTotal = remCard.render(str(blackjack.getHandTotal(playerHand)), True, 'Black')
    handValues = remCard.render(str(playerHand), True, 'Black')
    screen.blit(remainingCards, [100, 300])
    screen.blit(handTotal, [100, 400])
    screen.blit(handValues, [100, 500])

    #UPDATE DISPLAY -- KEEP LAST
    pygame.display.flip()

    #EXIT GAME
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
pygame.quit()