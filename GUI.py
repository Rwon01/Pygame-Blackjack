import pygame
import pydealer
from Game import Game
import os
from Button import Button
from renderText import Text
from Blackjack import Blackjack
from Card import Card
from settings import *

class GUI():

    def __init__(self):
        pygame.init()

    def run(self):

        os.environ['SDL_VIDEO_CENTER'] = '1'
        info = pygame.display.Info()
        SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT - 50), pygame.RESIZABLE)
        pygame.display.set_caption("Blackjack Game")
        clock = pygame.time.Clock()
        run = True

        #CREATE INSTANCES 
    
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
        hand_count = Text(str(game.player.get_hand_value()), position=[SCREEN_WIDTH*0.2, SCREEN_HEIGHT-100], color='Black', fontSize=18)
        dealer_hand_count = Text(text="", position=[SCREEN_WIDTH*0.2, 700], color='Red', fontSize=18)
        Remaining_count = Text("Remaining cards: " + str(Blackjack.pile.size), position=[SCREEN_WIDTH*0.5, SCREEN_HEIGHT-100], color='Black', fontSize=18)

        #GUI CONST
        POS_X = SCREEN_WIDTH * 0.50
        rect_size = btnDouble.rect.w + 30
        #GUI
        btnHit.move([POS_X - 2 * rect_size , SCREEN_HEIGHT - 200])
        btnStand.move([POS_X - 1 * rect_size, SCREEN_HEIGHT - 200])
        btnDouble.move([POS_X, SCREEN_HEIGHT - 200])
        btnSplit.move([POS_X + 1 * rect_size, SCREEN_HEIGHT - 200])
        btnSurrender.move([POS_X + 2* rect_size, SCREEN_HEIGHT - 200])
        btnDeal.move([100, 100])

        while run:

            clock.tick(FPS)
            screen.fill("dark gray")
            
            for button in Button.button_group:
                button.render(screen) 
                action = button.is_clicked()
                if action == "HIT":
                    game.hit()
                    
                if action == 'DEAL':
                    game.deal_round()

                 

            for card_instance in Card.card_group:
                card_instance.render(screen)


            hand_count.text = "Your hand value: " + str(game.player.get_hand_value())
            dealer_hand_count.text = "Dealer hand value: " + str(game.dealer.get_hand_value())
            Remaining_count.text = ("Remaining cards: " + str(Blackjack.pile.size))
            dealer_hand_count.render(screen)
            hand_count.render(screen)
            Remaining_count.render(screen)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.flip()
            

if __name__ == "__main__":
    game = Game()
    gui = GUI()
    gui.run()