import math
import pygame

from ..object import GameObject
from scripts import SoundManager
from utils import approach, polygon_coordinate, angle_rotate

class Entity(GameObject):
    def __init__(self, x, y, color, angle, min_angle, max_angle):
        super().__init__()
        
        self.x = x
        self.y = y
        self.color = color
        self.arc_angle = angle
        self.min_angle = min_angle
        self.max_angle = max_angle

        self.radius = 200

        self.cooldown = 0
        self.max_cooldown = 20
        
        self.polygon_angle = 0
        self.polygon_smooth = 0
        self.polygon_points = 12

        self.snd_shoot = [SoundManager.load_sound('snd_shoot' + str(i) + '.wav') for i in range(1, 5)]
    
    def pre_update(self, events):
        pass

    def update(self, delta_time):
        # Gear movement
        self.polygon_angle = angle_rotate(self.polygon_angle, self.polygon_smooth, 0.15 * delta_time)
        
        # Reduce cooldown
        self.cooldown = approach(self.cooldown, 0, 0.06 * delta_time)

    def draw(self, surface):
        # List of poinst for the circle
        points = []
        for i in range(self.polygon_points):
            angle = self.polygon_angle + i * 360 / self.polygon_points
            points.append(polygon_coordinate(self.x, self.y, angle, self.radius))
        
        # Draw the gear
        pygame.draw.polygon(surface, self.color, points)
        
        # Shooter recoil after shooting
        recoil = 1.05 * min(1, 1 - self.cooldown / self.max_cooldown * 0.03)

        # Rectangle to indicate the position and dimensions of the ellipse
        left = self.x - self.radius * recoil
        right = self.y - self.radius * recoil
        height = self.radius * recoil * 2
        width = self.radius * recoil * 2

        rectangle = pygame.Rect(left, right, width, height)

        # Draw the shooter
        start_angle = math.radians(self.arc_angle + 5)
        stop_angle = math.radians(self.arc_angle + 25)
        width = max(1, round(self.cooldown / self.max_cooldown * 3))

        pygame.draw.arc(surface, self.color, rectangle, start_angle, stop_angle, width)