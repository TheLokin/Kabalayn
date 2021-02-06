from ..object import GameObject
from utils import approach, ease_in_quad, ease_out_quad

class Portrait(GameObject):
    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y

        self.paused = False

        self.frame = 0
        self.max_frames = 45
        self.animation = 0
    
    def pre_update(self, events):
        pass

    def pause(self):
        self.paused = not self.paused

    def update(self, delta_time):
        if not self.paused:
            # Change animation
            if self.frame == self.max_frames:
                self.frame = 0

                # From animation go down to animation go up
                if self.animation == 0:
                    self.animation = 1
            
                # From animation go up to animation go down
                elif self.animation == 1:
                    self.animation = 0
            else:
                # Calculate the next frame
                self.frame = approach(self.frame, self.max_frames, 0.06 * delta_time)

    def draw(self, surface, sprite):
        # Animation go down
        if self.animation == 0:
            distance = ease_in_quad(self.frame, 0, 5, self.max_frames)
            surface.blit(sprite, (self.x, self.y + distance))
        
        # Animation go up
        elif self.animation == 1:
            distance = 5 - ease_out_quad(self.frame, 0, 5, self.max_frames)
            surface.blit(sprite, (self.x, self.y + distance))