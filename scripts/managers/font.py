import os
import pygame

class FontManager(object):
    resources = {}

    @classmethod
    def load_font(cls, name, size):
        '''
            If the file name is among the resources already loaded, that is returned and if
            it has not been previously loaded, the font is loaded indicating from the
            'datafiles/fonts' folder.

            name: The name of the font.

            size: The size of the font. Pixels for *.ttf fonts.
        '''

        code = hash(name + str(size))

        if code in cls.resources:
            return cls.resources[code]
        else:
            path = os.path.join('datafiles', 'fonts', name)

            try:
                font = pygame.font.Font(path, size)
            except FileNotFoundError:
                raise Exception('Cannot load font: ' + path)
                
            cls.resources[code] = font

            return font
        