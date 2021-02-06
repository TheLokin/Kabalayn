import random
import pygame

from ..object import GameObject
from scripts import SpriteManager
from utils import Colors, approach, swap_color, slice_sprite

class Dust(GameObject):
    def __init__(self, x, y, color, hspeed, vspeed, image_speed):
        super().__init__()
        
        self.x = x - 4
        self.y = y - 4
        self.color = color
        self.hspeed = hspeed
        self.vspeed = vspeed
        
        sprite = swap_color(SpriteManager.load_sprite('spr_particle.png'), Colors.WHITE, color)
        self.sprite_sheet = slice_sprite(sprite, 8, 8)
        self.image_index = 0
        self.image_speed = image_speed
    
    def pre_update(self, events):
        pass
    
    def update(self, delta_time):
        # Calculate the new position
        self.x += self.hspeed * 0.06 * delta_time
        self.y += self.vspeed * 0.06 * delta_time
    
        # Calculate the current sub-image
        self.image_index = approach(self.image_index, len(self.sprite_sheet), self.image_speed * delta_time)

        # Destroy dust particle
        if self.image_index == len(self.sprite_sheet):
            self.destroy()

    def draw(self, surface):
        # Draw the dust particle
        surface.blit(self.sprite_sheet[int(self.image_index)], (self.x, self.y))