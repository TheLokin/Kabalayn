import random
import scenes

from utils import Colors
from ..scene_fade import SceneFade
from objects import Player1, Player2
from .screen_intro import ScreenIntro
from scripts import Keyboard, SoundManager
from .screen_infinite import ScreenInfinite
from scripts import Configuration as Config

class StageMultiplayer(SceneFade):
    def __init__(self):
        super().__init__()

        # Load the screen for the multiplayer stage
        entities = (
            Player1(Colors.VIR),
            Player2(Config.state()['color'])
        )
        balls = [
            (65, 175, 10),
            (185, 175, 10)
        ]
        self.current_screen = ScreenIntro(entities, balls)
        self.screen_play = ScreenInfinite(entities, balls, 10)
        
        # Pause sound
        self.snd_click = SoundManager.load_sound('snd_click.wav')

        # Play the background music
        SoundManager.load_music('bgm_stage1.ogg')
    
    def start(self):
        # Change the current screen
        self.current_screen = self.screen_play

        # Change the background music
        SoundManager.load_music('bgm_stage' + str(random.randint(2, 6)) + '.ogg')
    
    def pre_update(self, events):
        super().pre_update(events)
        
        # Pre update the current screen
        self.current_screen.pre_update(events)
        
        # Pause the game
        if Keyboard.check_pressed('pause', events):
            self.director.push_scene(scenes.Pause())
            self.snd_click.play()
    
    def update(self, delta_time):
        super().update(delta_time)

        # Update the current screen
        self.current_screen.update(delta_time, self)

    def draw(self, screen):
        # Draw the current screen
        self.current_screen.draw(screen)

        super().draw(screen)