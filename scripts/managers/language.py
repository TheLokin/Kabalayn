import os
import json

from ..configuration import Configuration as Config

class LanguageManager(object):
    resources = None

    @classmethod
    def languages(cls):
        '''
            Returns a list with the available languages.
        '''
        
        path = os.path.join('datafiles', 'lang')

        return [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]

    @classmethod
    def change_language(cls, lang):
        '''
            Sets the langugage of the game.

            lang: The new language.
        '''

        if os.path.isfile(os.path.join('datafiles', 'lang', lang)):
            Config.lang = lang
            cls.resources = None

    @classmethod
    def load_text(cls, name):
        '''
            If the lang file is among the resources already loaded, the value associated with the
            name is returned. The lang file is loaded indicating from the 'datafiles/lang' folder.

            name: The name of the text.
        '''

        if cls.resources is None:
            path = os.path.join('datafiles', 'lang', Config.lang)

            try:
                with open(path, 'r', encoding='utf-8') as file:
                    cls.resources = json.load(file)
            except FileNotFoundError:
                raise Exception('Cannot load lang: ' + path)
    
        return cls.resources[name]