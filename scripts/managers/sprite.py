import os
import pygame

class SpriteManager(object):
    resources = {}

    @classmethod
    def load_sprite(cls, name):
        '''
            If the file name is among the resources already loaded, that is returned and if
            it has not been previously loaded, the sprite is loaded indicating from the
            'datafiles/sprites' folder.

            name: The name of the sprite.
        '''

        code = hash(name)

        if code in cls.resources:
            return cls.resources[code].copy()
        else:
            path = os.path.join('datafiles', 'sprites', name)
            
            try:
                sprite = pygame.image.load(path).convert_alpha()
            except FileNotFoundError:
                raise Exception('Cannot load sprite: ' + path)

            cls.resources[code] = sprite

            return sprite.copy()