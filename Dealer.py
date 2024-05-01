from Player import Player

class Dealer(Player):

    def __init__(self, starting_position):
        super().__init__()
        self.starting_position = starting_position
        self.hidden_card = None

    def render_cards(self):
        index = 0
        for card in self.hand:
            if index == 0 : card_sprite = self.convert_to_card_sprite(card, True)
            else:card_sprite = self.convert_to_card_sprite(card, False)
            size = card_sprite.rect.w + 15
            card_sprite.move([self.starting_position[0] + size * index, self.starting_position[1]])
            index += 1


    def reveal_card(self):
        #TODO
        pass