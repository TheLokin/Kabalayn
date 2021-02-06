import scenes

from objects import Enemy, Player
from ..scene_fade import SceneFade
from utils import Singleton, Colors
from .screen_menu import ScreenMenu
from ..stage import ScreenBackground
from pygame.locals import BLEND_MULT
from .screen_options import ScreenOptions
from scripts import SoundManager, Configuration as Config

class Menu(SceneFade):
    loaded = False

    def __new__(cls, victory=True):
        if not cls.loaded:
            cls.loaded = True
            Config.load()

        return super().__new__(cls)

    def __init__(self, victory=False):
        super().__init__()
        
        # Background
        state = Config.state()
        self.background = ScreenBackground((Player(Colors.VIR), Enemy(state['color'], state['shoot_delay'])))

        # Screens
        self.screen_menu = ScreenMenu(self)
        self.screen_options = ScreenOptions(self)

        # Set the current screen
        self.current_screen = self.screen_menu

        # Play the background music
        if victory:
            SoundManager.load_music('bgm_victory.ogg')
        else:
            SoundManager.load_music('bgm_menu.ogg')

    def exec_play(self):
        self.director.change_scene(scenes.Cutscene())

    def exec_multiplayer(self):
        self.director.change_scene(scenes.StageMultiplayer())

    def exec_options(self):
        self.current_screen = self.screen_options

    def exec_exit(self):
        self.director.game_end()
    
    def exec_cancel(self):
        self.current_screen = self.screen_menu

    def exec_confirm(self):
        self.current_screen = self.screen_menu

    def pre_update(self, events):
        super().pre_update(events)
        
        # Pre update the current screen
        self.current_screen.pre_update(events, self)

    def update(self, delta_time):
        super().update(delta_time)

        # Update the current screen
        self.current_screen.update(delta_time)
        
    def draw(self, screen):
        # Draw background
        self.background.draw(screen)

        # Draw shadow over background
        shadow = screen.copy()
        shadow.fill(Colors.LIGHT_GREY)
        shadow.blit(screen, (0, 0), special_flags=BLEND_MULT)
        screen.blit(shadow, (0, 0))

        # Draw the current screen
        self.current_screen.draw(screen)

        super().draw(screen)