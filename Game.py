from Player import Player
from Dealer import Dealer
from Blackjack import Blackjack
from settings import *
from Card import Card

class Game:

    def __init__(self):
        self.deck = Blackjack.pile
        self.dealer = Dealer(starting_position=[SCREEN_WIDTH*0.25, 150])
        self.player = Player(starting_position=[SCREEN_WIDTH*0.25, 500])
        self.game_over = False
        self.state = None

    def hit(self):
        if not self.game_over and self.player.get_hand_value() < 21:
            self.player.add_card()
            
            if self.player.get_hand_value() > 21:
                self.game_over = True
                self.dealer.reveal_card()
                
                self.state = 'Player bust'
            else:
                self.state = ''
        else:
                self.state = ''

    def stand(self):
        if not self.game_over:
            self.dealer.reveal_card()
            
            while self.dealer.get_hand_value() < 17:
                self.dealer.add_card()
                
            player_value = self.player.get_hand_value()
            dealer_value = self.dealer.get_hand_value()
            if dealer_value > 21 or player_value > dealer_value:
                self.game_over = True
                self.state = 'Player win'
            elif dealer_value > player_value:
                self.game_over = True
                self.state =  "Dealer wins!"
            else:
                self.game_over = True
                self.state =  "It's a tie!"
        else:
            return None

    def calculate_winner(self):
        pass

    def deal_round(self):
        Blackjack.pile.shuffle()
        self.player.add_card()
        self.player.add_card()
        self.dealer.add_card()
        self.dealer.add_card()
        self.check_blackjack()
        self.render_cards()

    def check_blackjack(self):
        if self.dealer.hand.size == 2 and self.dealer.get_hand_value() == 21:
            self.dealer.reveal_card()
            self.state = "Dealer blackjack"
            self.game_over = True
            self.restart_game()
        if self.player.hand.size == 2 and self.player.get_hand_value() == 21:
            self.state = "Player blackjack"
            self.game_over = True
            self.restart_game()

    def convert_to_card_sprite(self, card, is_hidden = False):
        cardpath = f"assets/cardsSet/{card.value}_of_{card.suit}.png".lower()
        card = Card(imageDirectory=cardpath, is_hidden=is_hidden)
        return card


    def restart_game(self):
        if self.game_over:
            self.player.empty_hand()
            self.dealer.empty_hand()
            self.game_over = False
            self.dealer.hidden_card = True
            self.deal_round()
        



    def render_cards(self):
        index_player = 0
        index_dealer = 0

        for card_img in Card.card_group:
            card_img.kill()
        
        for card in self.player.hand:
            card_sprite = self.convert_to_card_sprite(card, False)
            size = card_sprite.rect.w + 15
            card_sprite.move([self.player.starting_position[0] + size * index_player, self.player.starting_position[1]])
            index_player += 1

        for card in self.dealer.hand:
            if self.dealer.hidden_card and index_dealer == 0:
                card_sprite = self.convert_to_card_sprite(card, True)
            else:
                card_sprite = self.convert_to_card_sprite(card, False)
            size = card_sprite.rect.w + 15
            card_sprite.move([self.dealer.starting_position[0] + size * index_dealer, self.dealer.starting_position[1]])
            index_dealer += 1