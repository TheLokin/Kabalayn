from .screen_play import ScreenPlay

class ScreenHardcore(ScreenPlay):
    def __init__(self, entities, balls, max_balls, max_score):
        super().__init__(entities, balls, max_balls)

        self.max_score = max_score
      
    def check_score(self, scene):
        if self.player_score == self.max_score:
            scene.stop(True)
        elif self.enemy_score == 1:
            scene.stop(False)