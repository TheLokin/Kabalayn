from ..object import GameObject
from scripts import Keyboard, SoundManager, FontManager, LanguageManager

class Button(GameObject):
    selected = None

    def __init__(self, text_code):
        super().__init__()

        self.is_selected = False

        self.opacity = 128
        self.text_code = text_code
        self.text = LanguageManager.load_text(text_code)
        self.font = FontManager.load_font('neogen.ttf', 24)

        self.snd_click = SoundManager.load_sound('snd_click.wav')
        self.snd_choice = SoundManager.load_sound('snd_choice.wav')

    def execute(self, scene):
        '''
            Method called when the button is executed.

            scene: The scene where the action is executed.
        '''

        pass

    def key_up(self, scene):
        '''
            Method called when the key up is pressed.

            scene: The scene where the action is executed.
        '''

        pass

    def key_down(self, scene):
        '''
            Method called when the key down is pressed.

            scene: The scene where the action is executed.
        '''

        pass

    def key_left(self, scene):
        '''
            Method called when the key left is pressed.

            scene: The scene where the action is executed.
        '''

        pass

    def key_right(self, scene):
        '''
            Method called when the key right is pressed.

            scene: The scene where the action is executed.
        '''

        pass

    def pre_update(self, events, scene):
        if self.is_selected and not scene.is_fading:
            # Execute
            if Keyboard.check_pressed('interact', events):
                self.execute(scene)
            
            # Key up
            elif Keyboard.check_pressed('up', events):
                self.key_up(scene)

            # Key down
            elif Keyboard.check_pressed('down', events):
                self.key_down(scene)
            
            # Key left
            elif Keyboard.check_pressed('left', events):
                self.key_left(scene)
            
            # Key right
            elif Keyboard.check_pressed('right', events):
                self.key_right(scene)

    def update(self, delta_time):
        # Update the selection
        self.is_selected = False
        Button.selected.is_selected = True

        # Update the text
        self.text = LanguageManager.load_text(self.text_code)