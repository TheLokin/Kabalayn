import scenes

from utils import Colors
from objects import Player, Enemy
from ..scene_fade import SceneFade
from .screen_intro import ScreenIntro
from .screen_normal import ScreenNormal
from scripts import Keyboard, SoundManager
from .screen_hardcore import ScreenHardcore
from scripts import Configuration as Config

class Stage(SceneFade):
    def __init__(self):
        super().__init__()

        # Load the screen for the current stage
        state = Config.state()
        entities = (Player(Colors.VIR), Enemy(state['color'], state['shoot_delay']))
        self.screen_intro = ScreenIntro(entities, state['balls'])
        if Config.level == 4:
            self.screen_play = ScreenHardcore(entities, state['balls'], state['max_balls'], state['max_score'])
        else:
            self.screen_play = ScreenNormal(entities, state['balls'], state['max_balls'], state['max_score'])

        # Set the current screen
        self.current_screen = self.screen_intro

        # Pause sound
        self.snd_click = SoundManager.load_sound('snd_click.wav')

        # Play the background music
        SoundManager.load_music('bgm_stage1.ogg')
    
    def start(self):
        # Change the current screen
        self.current_screen = self.screen_play

        # Change the background music for the current stage
        SoundManager.load_music(Config.state()['music'])
    
    def stop(self, victory):
        # Load the next cutscene
        if victory:
            self.director.change_scene(scenes.Cutscene())
        
        # Load the lose cutscene
        else:
            self.director.change_scene(scenes.Cutscene(False))

    def pre_update(self, events):
        super().pre_update(events)
        
        # Pre update the current screen
        self.current_screen.pre_update(events)
        
        # Pause the game
        if Keyboard.check_pressed('pause', events):
            self.director.push_scene(scenes.Pause(True))
            self.snd_click.play()
    
    def update(self, delta_time):
        super().update(delta_time)
        
        # Update the current screen
        self.current_screen.update(delta_time, self)

    def draw(self, screen):
        # Draw the current screen
        self.current_screen.draw(screen)

        super().draw(screen)