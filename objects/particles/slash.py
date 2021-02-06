import pygame

from ..object import GameObject
from utils import approach, polygon_coordinate

class Slash(GameObject):
    def __init__(self, x, y, color, angle, duration):
        super().__init__()
        
        self.x = x
        self.y = y
        self.color = color
        self.angle = angle
        self.duration = duration
    
    def pre_update(self, events):
        pass
    
    def update(self, delta_time):
        # Calculate the new position
        self.x, self.y = polygon_coordinate(self.x, self.y, self.angle, 0.24 * delta_time)

        # Reduce time left
        self.duration = approach(self.duration, 0, 0.2 * delta_time)

        # Destroy slash particle
        if self.duration == 0:
            self.destroy()
    
    def draw(self, surface):
        # Draw a diamond shape
        points = []

        # Right point
        points.append(polygon_coordinate(self.x, self.y, self.angle, self.duration))

        # Bottom point
        points.append(polygon_coordinate(self.x, self.y, self.angle + 90, 1))

        # Left point
        points.append(polygon_coordinate(self.x, self.y, self.angle + 180, 10))
        
        # Top point
        points.append(polygon_coordinate(self.x, self.y, self.angle + 270, 1))

        pygame.draw.polygon(surface, self.color, points)