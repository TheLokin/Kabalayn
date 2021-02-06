import pygame

from .button import Button
from utils import blit_alpha
from ..object import GameObject
from scripts import SpriteManager, SoundManager

class Arrow(GameObject):
    def __init__(self, button):
        super().__init__()

        self.button = button

        self.snd_click = SoundManager.load_sound('snd_click.wav')
    
    def pre_update(self, events):
        pass
    
    def update(self, delta_time):
        pass
    
    def draw(self, surface):
        # Draw the arrow
        if self.button.is_selected:
            if not self.button.is_circular:
                if self.button.option == self.limit_option:
                    blit_alpha(surface, self.spr_arrow, self.x, self.y, self.button.opacity)
                else:
                    surface.blit(self.spr_arrow, (self.x, self.y))
            else:
                surface.blit(self.spr_arrow, (self.x, self.y))
        else:
            blit_alpha(surface, self.spr_arrow, self.x, self.y, self.button.opacity)

class ArrowLeft(Arrow):
    def __init__(self, button, x, y):
        super().__init__(button)

        self.limit_option = 0

        self.spr_arrow = SpriteManager.load_sprite('spr_arrow.png')
        self.spr_arrow = pygame.transform.flip(self.spr_arrow, True, False)
        self.x = x - self.spr_arrow.get_width() - 8
        self.y = y - self.spr_arrow.get_height() / 2

class ArrowRight(Arrow):
    def __init__(self, button, x, y):
        super().__init__(button)

        self.limit_option = len(self.button.options) - 1

        self.spr_arrow = SpriteManager.load_sprite('spr_arrow.png')
        self.x = x + 8
        self.y = y - self.spr_arrow.get_height() / 2