import pygame
import random
import os
from Card import Card
from settings import *
from Button import Button
from Blackjack import Blackjack
import time
from renderText import Text
from Player import Player
from timer import Timer
import pydealer

def end_round_all():
    player.end_round()
    dealer.end_round()

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
player = Player(starting_position=[SCREEN_WIDTH*0.25, 500])
dealer = Player(starting_position=[SCREEN_WIDTH*0.25, 150])

#GROUPS
textGroup = pygame.sprite.Group()
#CREATE BUTTON
btnHit = Button(text="HIT")
btnStand = Button(text="STAND")
btnDouble = Button(text="DOUBLE")
btnSplit = Button(text="SPLIT")
btnSurrender = Button(text="SURRENDER", text_size=18)
btnDeal = Button(text="DEAL", text_size=32)

#TEXT
hand_count = Text(str(player.get_hand_value()), position=[SCREEN_WIDTH*0.2, SCREEN_HEIGHT-100], color='Black', fontSize=18)
Remaining_count = Text("Remaining cards: " + str(Blackjack.pile.size), position=[SCREEN_WIDTH*0.5, SCREEN_HEIGHT-100], color='Black', fontSize=18)
test = Text("BUST", [SCREEN_WIDTH*0.10, 500], 'Red', 50)

#GUI CONST
POS_X = SCREEN_WIDTH * 0.50
CARD_X = SCREEN_WIDTH * 0.20 - 20 // 2
card_size = card_for_width.rect.w + card_for_width.rect.w * 0.15
rect_size = btnDouble.rect.w + 30
#GUI
btnHit.move([POS_X - 2 * rect_size , SCREEN_HEIGHT - 200])
btnStand.move([POS_X - 1 * rect_size, SCREEN_HEIGHT - 200])
btnDouble.move([POS_X, SCREEN_HEIGHT - 200])
btnSplit.move([POS_X + 1 * rect_size, SCREEN_HEIGHT - 200])
btnSurrender.move([POS_X + 2* rect_size, SCREEN_HEIGHT - 200])
btnDeal.move([100, 100])


#GAMELOOP

simple_timer = Timer(800, end_round_all)
run = True
while run:
    clock.tick(FPS)
    mousePos = pygame.mouse.get_pos()
    #BACKGROUND
    screen.fill("dark gray")
   
    for card_instance in Card.card_group:
        card_instance.render(screen)

    #BUTTON LOOP
    for button in Button.button_group:
        test_value = button.is_clicked()
        if test_value == "DEAL":
            for _ in range(2):
                player.hit()
                dealer.hit()
        if test_value == "HIT":
            player.hit()
        if test_value == "STAND":
            player.has_busted = True

        if test_value == "DOUBLE":
            pass

        button.render(screen)

    hand_count.text = "Your hand value: " + str(player.get_hand_value())
    Remaining_count.text = ("Remaining cards: " + str(Blackjack.pile.size))
    hand_count.render(screen)
    Remaining_count.render(screen)

    simple_timer.update()

    if player.has_busted:
        simple_timer.activate()
        player.has_busted = False

    if simple_timer.active:
        test.render(screen)

    #UPDATE DISPLAY -- KEEP LAST
    pygame.display.flip()

    #EXIT GAME
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

            
pygame.quit()