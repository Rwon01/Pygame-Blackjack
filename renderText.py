import pygame

class Text(pygame.sprite.Sprite):
    
    def __init__(self, text, position, color, fontSize):
        super().__init__()
        self.font_size = fontSize
        self.text = text
        self.position = position
        self.color = color
        self.font = pygame.font.SysFont("Arial Black", self.font_size)
        self.render_font = self.font.render(self.text, True, self.color)
    
    def render(self, surface):
        surface.blit(self.font.render(self.text, True, self.color), self.position)
    