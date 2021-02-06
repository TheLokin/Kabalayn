import pygame

from ..object import GameObject
from utils import approach, ease_in_out_circle

class Explosion(GameObject):
    def __init__(self, x, y, color, start, target):
        super().__init__()

        self.x = x
        self.y = y
        self.color = color
        
        self.radius = 0
        self.frame = 0
        self.start = start
        self.target = target
        self.duration = start + 40

    def pre_update(self, events):
        pass

    def update(self, delta_time):
        # Increase the radius of the explosion
        self.radius = ease_in_out_circle(self.frame, self.start, self.target, self.duration)
        
        # Calculate the next frame
        self.frame = approach(self.frame, self.duration, 0.06 * delta_time)

        # Destroy explosion particle
        if self.frame == self.duration:
            self.destroy()

    def draw(self, surface):
        # Draw the explosion particle
        width = round(2 * self.frame / self.duration) + 1
        pygame.draw.circle(surface, self.color, (round(self.x), round(self.y)), round(max(self.radius, width)), width)