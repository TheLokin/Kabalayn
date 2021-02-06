import os
import pygame

from ..configuration import Configuration as Config

class SoundManager(object):
    resources = {}

    @classmethod
    def set_master(cls, master_volume):
        '''
            Sets the volume of the master.

            master_volume: The new master volume, from 0 to 1.
        '''

        Config.master_volume = master_volume
        master_volume = master_volume * Config.sound_volume
        
        for sound in list(cls.resources.values()):
            sound.set_volume(master_volume)
        
        pygame.mixer.music.set_volume(master_volume * Config.music_volume)

    @classmethod
    def set_sound(cls, sound_volume):
        '''
            Sets the volume of the sounds.

            sound_volume: The new sound volume, from 0 to 1.
        '''

        Config.sound_volume = sound_volume
        sound_volume = Config.master_volume * sound_volume
        
        for sound in list(cls.resources.values()):
            sound.set_volume(sound_volume)
        
    @classmethod
    def set_music(cls, music_volume):
        '''
            Sets the volume of the music.

            music_volume: The new music volume, from 0 to 1.
        '''

        Config.music_volume = music_volume
        
        pygame.mixer.music.set_volume(Config.master_volume * music_volume)

    @classmethod
    def load_sound(cls, name):
        '''
            If the file name is among the resources already loaded, that is returned and if
            it has not been previously loaded, the sound is loaded indicating from the
            'datafiles/sounds' folder.

            name: The name of the sound.
        '''

        code = hash(name)

        if code in cls.resources:
            return cls.resources[code]
        else:
            path = os.path.join('datafiles', 'sounds', name)

            try:
                sound = pygame.mixer.Sound(path)
            except FileNotFoundError:
                raise Exception('Cannot load sound: ' + path)
                
            cls.resources[code] = sound
            sound.set_volume(Config.master_volume * Config.sound_volume)

            return sound
    
    @classmethod
    def load_music(cls, name):
        '''
            The music is loaded indicating from the 'datafiles/sounds' folder and plays
            the loaded music in a loop.

            name: The name of the music.
        '''

        pygame.mixer.music.stop()

        path = os.path.join('datafiles', 'sounds', name)

        try:
            pygame.mixer.music.load(path)
        except FileNotFoundError:
            raise Exception('Cannot load music:' + path)
        
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(Config.master_volume * Config.music_volume)