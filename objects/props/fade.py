from ..object import GameObject
from scripts import SpriteManager
from utils import approach, clamp, slice_sprite

class Fade(GameObject):
    reverse = False

    def __init__(self, row):
        super().__init__()

        self.x = 32 * row
        self.sprite_sheet = slice_sprite(SpriteManager.load_sprite('spr_transition.png'), 32, 32)

        self.image_index = 0
        self.image_speed = 0.025

        self.timer = 0

    def pre_update(self, events):
        pass
    
    def update(self, delta_time):
        # Calculate the current sub-image
        self.image_index = clamp(self.image_index + self.image_speed * delta_time, 0, len(self.sprite_sheet) - 1)
        
        # Keep the screen black
        if self.image_index == len(self.sprite_sheet) - 1:
            self.image_speed = 0
            self.timer = approach(self.timer, 25, 0.06 * delta_time)
            if self.timer == 25:
                self.image_speed = -0.015
                Fade.reverse = True
        
        # Destroy fade animation
        if self.image_speed < 0 and self.image_index == 0:
            self.destroy()

    def draw(self, surface):
        # Draw the fade column
        for i in range(22):
            surface.blit(self.sprite_sheet[int(self.image_index)], (self.x, 32 * i))