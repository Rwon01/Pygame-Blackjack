import pygame
import random
import os
from Card import Card
from settings import *
from Button import Button
from Blackjack import *


def convertToCardImage(card):
    cardpath = f"assets/cardsSet/{card.value}_of_{card.suit}.png".lower()
    card = Card(imageDirectory=cardpath)
    card.pyCard = card
    return card

def killSprites(spriteGroup):
        for sprite in spriteGroup:
            sprite.kill()

def discardHand(hand, isPlayer):
    blackjack.discard_pile.add(hand.empty(return_cards=True))
    if isPlayer:
        killSprites(cardGroupPlayer)
    elif not isPlayer:
        killSprites(cardGroupDealer)

def renderCards(hand, isPlayer):
    index = 0
    if isPlayer: killSprites(cardGroupPlayer)
    elif not isPlayer: killSprites(cardGroupDealer)

    for everycard in hand:

        d = convertToCardImage(everycard)
        if isPlayer:
            d.move([CARD_X + (index * card_size), SCREEN_HEIGHT - 500])
            cardGroupPlayer.add(d)
        elif not isPlayer:
            if index == 0: d.isHidden = True
            d.move([CARD_X + (index * card_size), SCREEN_HEIGHT - 800])
            cardGroupDealer.add(d)
        index += 1

def dealerMove():
    index = 0
    for card in cardGroupDealer:
        if index == 0 : card.isHidden = True

#BOILERPLATE FOR PYGAME
pygame.init()
os.environ['SDL_VIDEO_CENTER'] = '1'
info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT - 50), pygame.RESIZABLE)
pygame.display.set_caption("Blackjack Game")
clock = pygame.time.Clock()

#CREATE INSTANCES 
card_for_width = Card()
blackjack = Blackjack(AMOUNT_OF_DECKS)
playerHand = pydealer.Stack()
dealerHand = pydealer.Stack()


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
CARD_X = SCREEN_WIDTH * 0.20 - 20 // 2
card_size = card_for_width.rect.w + card_for_width.rect.w * 0.15

rect_size = btnDouble.rect.w
#GUI
btnHit.move([POS_X - 2 * rect_size , SCREEN_HEIGHT - 200])
btnStand.move([POS_X - 1 * rect_size, SCREEN_HEIGHT - 200])
btnDouble.move([POS_X, SCREEN_HEIGHT - 200])
btnSplit.move([POS_X + 1 * rect_size, SCREEN_HEIGHT - 200])
btnSurrender.move([POS_X + 2* rect_size, SCREEN_HEIGHT - 200])
btnDeal.move([100, 100])

buttonGroup = pygame.sprite.Group()
cardGroupPlayer = pygame.sprite.Group()
cardGroupDealer = pygame.sprite.Group()
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
            dealerHand.add(blackjack.dealCard(2))
            renderCards(playerHand, isPlayer=True)
            renderCards(dealerHand, isPlayer=False)
                      
        if test_value == "HIT":
            if blackjack.getHandTotal(playerHand) <= 21:
                playerHand.add(blackjack.dealCard(1))
                renderCards(playerHand, isPlayer=True)
            else:
                print('GOING OVER 21')
        
        if test_value == 'STAND':
            discardHand(playerHand, isPlayer=True)
            blackjack.pile.shuffle()
        if test_value == 'DOUBLE':
            dealerMove()
        button.render(screen)


    for visible_card in cardGroupPlayer:
        visible_card.render(screen)
    for visible_card in cardGroupDealer:
        visible_card.render(screen)

    remainingCards = remCard.render("Remaining cards: " + str(len(blackjack.pile)), True, 'Black')
    handTotal = remCard.render("Your hand total is: " + str(blackjack.getHandTotal(playerHand)), True, 'Black')
    screen.blit(remainingCards, [100, 300])
    screen.blit(handTotal, [100, 400])

    #UPDATE DISPLAY -- KEEP LAST
    pygame.display.flip()

    #EXIT GAME
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
pygame.quit()