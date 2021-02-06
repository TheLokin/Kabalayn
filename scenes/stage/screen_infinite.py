from .screen_play import ScreenPlay

class ScreenInfinite(ScreenPlay):
    def __init__(self, entities, balls, max_balls):
        super().__init__(entities, balls, max_balls)
    
    def check_score(self, scene):
        pass