from .button import Button
from .button_action import ButtonAction
from .button_option import ButtonOption
from scripts import LanguageManager, SoundManager, Configuration as Config

class ButtonPlay(ButtonAction):
    instances = {}
    
    def __new__(cls, scene):
        if scene not in cls.instances:
            cls.instances[scene] = super().__new__(cls)
        Button.selected = cls.instances[scene]
        
        return cls.instances[scene]

    def __init__(self, scene):
        super().__init__(114, 262, 15, 1, 'uiPlay')

    def execute(self, scene):
        self.snd_click.play()
        scene.fade(self.execute_async, scene)
    
    def execute_async(self, scene):
        SoundManager.load_music('bgm_dialog.ogg')
        scene.exec_play()

    def key_up(self, scene):
        self.snd_choice.play()
        Button.selected = ButtonExit(scene)
        
    def key_down(self, scene):
        self.snd_choice.play()
        Button.selected = ButtonMultiplayer(scene)

class ButtonMultiplayer(ButtonAction):
    instances = {}
    
    def __new__(cls, scene):
        if scene not in cls.instances:
            cls.instances[scene] = super().__new__(cls)
        
        return cls.instances[scene]
    
    def __init__(self, scene):
        super().__init__(114, 326, 15, 1, 'uiMultiplayer')

    def execute(self, scene):
        self.snd_click.play()
        scene.fade(scene.exec_multiplayer)
    
    def key_up(self, scene):
        self.snd_choice.play()
        Button.selected = ButtonPlay(scene)

    def key_down(self, scene):
        self.snd_choice.play()
        Button.selected = ButtonOptions(scene)

class ButtonOptions(ButtonAction):
    instances = {}
    
    def __new__(cls, scene):
        if scene not in cls.instances:
            cls.instances[scene] = super().__new__(cls)
        
        return cls.instances[scene]
    
    def __init__(self, scene):
        if scene.__class__.__name__ == 'Menu':
            super().__init__(114, 390, 15, 1, 'uiOptions')
        elif scene.__class__.__name__ == 'Pause':
            super().__init__(114, 326, 15, 1, 'uiOptions')

    def execute(self, scene):
        self.snd_click.play()
        scene.fade(self.execute_async, scene)
    
    def execute_async(self, scene):
        Button.selected = ButtonLanguage(scene)
        scene.exec_options()

    def key_up(self, scene):
        self.snd_choice.play()
        
        if scene.__class__.__name__ == 'Menu':
            Button.selected = ButtonMultiplayer(scene)
        elif scene.__class__.__name__ == 'Pause':
            Button.selected = ButtonContinue(scene)

    def key_down(self, scene):
        self.snd_choice.play()
        
        if scene.__class__.__name__ == 'Menu':
            Button.selected = ButtonExit(scene)
        elif scene.__class__.__name__ == 'Pause':
            Button.selected = ButtonQuit(scene)

class ButtonExit(ButtonAction):
    instances = {}
    
    def __new__(cls, scene):
        if scene not in cls.instances:
            cls.instances[scene] = super().__new__(cls)
        
        return cls.instances[scene]
    
    def __init__(self, scene):
        super().__init__(114, 454, 15, 1, 'uiExit')

    def execute(self, scene):
        self.snd_click.play()
        Config.save()
        scene.exec_exit()
    
    def key_up(self, scene):
        self.snd_choice.play()
        Button.selected = ButtonOptions(scene)
    
    def key_down(self, scene):
        self.snd_choice.play()
        Button.selected = ButtonPlay(scene)

class ButtonLanguage(ButtonOption):
    instances = {}
    
    def __new__(cls, scene):
        if scene not in cls.instances:
            cls.instances[scene] = super().__new__(cls)
        
        return cls.instances[scene]
    
    def __init__(self, scene):
        options = LanguageManager.languages()
        super().__init__(74, 198, 20, 1, options.index(Config.lang), options, True, 'configLanguage')

        self.original = Config.lang

    @classmethod
    def cancel(cls, scene):
        button = cls.instances[scene]
        button.option = button.options.index(button.original)
        LanguageManager.change_language(button.original)

    @classmethod
    def confirm(cls, scene):
        button = cls.instances[scene]
        button.original = LanguageManager.languages()[button.option]

    def execute(self, scene):
        self.snd_choice.play()
        LanguageManager.change_language(self.options[self.option])

    def key_up(self, scene):
        self.snd_choice.play()
        Button.selected = ButtonConfirm(scene)
    
    def key_down(self, scene):
        self.snd_choice.play()
        Button.selected = ButtonMasterVolume(scene)

    def update(self, delta_time):
        super().update(delta_time)

        self.text_secondary = LanguageManager.load_text('optionLanguage')

class ButtonMasterVolume(ButtonOption):
    instances = {}
    
    def __new__(cls, scene):
        if scene not in cls.instances:
            cls.instances[scene] = super().__new__(cls)
        
        return cls.instances[scene]
    
    def __init__(self, scene):
        super().__init__(74, 262, 20, 1, Config.master_volume * 10, list(range(11)), False, 'configMasterVolume')

        self.original = Config.master_volume

    @classmethod
    def cancel(cls, scene):
        button = cls.instances[scene]
        button.option = int(button.original * 10)
        SoundManager.set_master(button.original)

    @classmethod
    def confirm(cls, scene):
        button = cls.instances[scene]
        button.original = button.option / 10

    def execute(self, scene):
        self.snd_click.play()
        SoundManager.set_master(self.option / 10)

    def key_up(self, scene):
        self.snd_choice.play()
        Button.selected = ButtonLanguage(scene)
    
    def key_down(self, scene):
        self.snd_choice.play()
        Button.selected = ButtonSoundVolume(scene)
    
    def update(self, delta_time):
        super().update(delta_time)

        self.text_secondary = str(self.option)

class ButtonSoundVolume(ButtonOption):
    instances = {}
    
    def __new__(cls, scene):
        if scene not in cls.instances:
            cls.instances[scene] = super().__new__(cls)
        
        return cls.instances[scene]
    
    def __init__(self, scene):
        super().__init__(74, 326, 20, 1, Config.sound_volume * 10, list(range(11)), False, 'configSoundVolume')

        self.original = Config.sound_volume

    @classmethod
    def cancel(cls, scene):
        button = cls.instances[scene]
        button.option = int(button.original * 10)
        SoundManager.set_sound(button.original)

    @classmethod
    def confirm(cls, scene):
        button = cls.instances[scene]
        button.original = button.option / 10

    def execute(self, scene):
        self.snd_click.play()
        SoundManager.set_sound(self.option / 10)

    def key_up(self, scene):
        self.snd_choice.play()
        Button.selected = ButtonMasterVolume(scene)
    
    def key_down(self, scene):
        self.snd_choice.play()
        Button.selected = ButtonMusicVolume(scene)
    
    def update(self, delta_time):
        super().update(delta_time)

        self.text_secondary = str(self.option)

class ButtonMusicVolume(ButtonOption):
    instances = {}
    
    def __new__(cls, scene):
        if scene not in cls.instances:
            cls.instances[scene] = super().__new__(cls)
        
        return cls.instances[scene]
    
    def __init__(self, scene):
        super().__init__(74, 390, 20, 1, Config.music_volume * 10, list(range(11)), False, 'configMusicVolume')

        self.original = Config.music_volume

    @classmethod
    def cancel(cls, scene):
        button = cls.instances[scene]
        button.option = int(button.original * 10)
        SoundManager.set_music(button.original)

    @classmethod
    def confirm(cls, scene):
        button = cls.instances[scene]
        button.original = button.option / 10

    def execute(self, scene):
        self.snd_click.play()
        SoundManager.set_music(self.option / 10)

    def key_up(self, scene):
        self.snd_choice.play()
        Button.selected = ButtonSoundVolume(scene)
    
    def key_down(self, scene):
        self.snd_choice.play()
        Button.selected = ButtonConfirm(scene)
    
    def update(self, delta_time):
        super().update(delta_time)

        self.text_secondary = str(self.option)

class ButtonConfirm(ButtonAction):
    instances = {}
    
    def __new__(cls, scene):
        if scene not in cls.instances:
            cls.instances[scene] = super().__new__(cls)
        
        return cls.instances[scene]
    
    def __init__(self, scene):
        super().__init__(50, 454, 10, 1, 'uiConfirm')

    def execute(self, scene):
        self.snd_click.play()
        Config.save()
        scene.fade(self.execute_async, scene)

    def execute_async(self, scene):
        ButtonLanguage.confirm(scene)
        ButtonMasterVolume.confirm(scene)
        ButtonSoundVolume.confirm(scene)
        ButtonMusicVolume.confirm(scene)
        Button.selected = ButtonOptions(scene)
        scene.exec_confirm()

    def key_up(self, scene):
        self.snd_choice.play()
        Button.selected = ButtonMusicVolume(scene)
    
    def key_down(self, scene):
        self.snd_choice.play()
        Button.selected = ButtonLanguage(scene)

    def key_left(self, scene):
        self.snd_choice.play()
        Button.selected = ButtonCancel(scene)

    def key_right(self, scene):
        self.snd_choice.play()
        Button.selected = ButtonCancel(scene)

class ButtonCancel(ButtonAction):
    instances = {}
    
    def __new__(cls, scene):
        if scene not in cls.instances:
            cls.instances[scene] = super().__new__(cls)
        
        return cls.instances[scene]
    
    def __init__(self, scene):
        super().__init__(258, 454, 10, 1, 'uiCancel')

    def execute(self, scene):
        self.snd_click.play()
        scene.fade(self.execute_async, scene)

    def execute_async(self, scene):
        ButtonLanguage.cancel(scene)
        ButtonMasterVolume.cancel(scene)
        ButtonSoundVolume.cancel(scene)
        ButtonMusicVolume.cancel(scene)
        Button.selected = ButtonOptions(scene)
        scene.exec_cancel()

    def key_up(self, scene):
        self.snd_choice.play()
        Button.selected = ButtonMusicVolume(scene)
    
    def key_down(self, scene):
        self.snd_choice.play()
        Button.selected = ButtonLanguage(scene)

    def key_left(self, scene):
        self.snd_choice.play()
        Button.selected = ButtonConfirm(scene)

    def key_right(self, scene):
        self.snd_choice.play()
        Button.selected = ButtonConfirm(scene)

class ButtonContinue(ButtonAction):
    instances = {}
    
    def __new__(cls, scene):
        if scene not in cls.instances:
            cls.instances[scene] = super().__new__(cls)
        
        Button.selected = cls.instances[scene]

        return cls.instances[scene]
    
    def __init__(self, scene):
        super().__init__(114, 262, 15, 1, 'uiContinue')

    def execute(self, scene):
        self.snd_click.play()
        scene.exec_continue()

    def key_up(self, scene):
        self.snd_choice.play()
        Button.selected = ButtonQuit(scene)
    
    def key_down(self, scene):
        self.snd_choice.play()
        Button.selected = ButtonOptions(scene)

class ButtonQuit(ButtonAction):
    instances = {}
    
    def __new__(cls, scene):
        if scene not in cls.instances:
            cls.instances[scene] = super().__new__(cls)
        
        return cls.instances[scene]
    
    def __init__(self, scene):
        super().__init__(114, 390, 15, 1, 'uiQuit')

    def execute(self, scene):
        self.snd_click.play()
        scene.fade(scene.exec_quit)

    def key_up(self, scene):
        self.snd_choice.play()
        Button.selected = ButtonOptions(scene)
    
    def key_down(self, scene):
        self.snd_choice.play()
        Button.selected = ButtonContinue(scene)