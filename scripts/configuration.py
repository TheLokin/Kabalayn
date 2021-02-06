import os
import json

from utils import Colors, clamp
from .controllers import Keyboard
from .managers.sprite_font import SpriteFontManager
from pygame.locals import K_UP, K_w, K_DOWN, K_s, K_LEFT, K_a, K_RIGHT, K_d, K_SPACE, K_e, K_RETURN, K_ESCAPE

def read_float(options, key, default):
    try:
        option = options[key]

        return option if isinstance(option, float) else default
    except KeyError:
        return default

def read_int(options, key, default):
    try:
        option = options[key]

        return option if isinstance(option, int) else default
    except KeyError:
        return default

def read_string(options, key, default):
    try:
        option = options[key]

        return option if isinstance(option, (str)) else default
    except KeyError:
        return default

class Configuration(object):
    lang = 'english.json'

    master_volume = 1
    sound_volume = 1
    music_volume = 1
    
    level = 1

    @classmethod
    def load(cls):
        # Load options
        if os.path.isfile('datafiles/options.json'):
            with open('datafiles/options.json', 'r', encoding='utf-8') as file:
                options = json.load(file)

                # Language options
                cls.lang = read_string(options, 'lang', cls.lang)
                if not os.path.isfile(os.path.join('datafiles', 'lang', cls.lang)):
                    cls.lang = 'english.json'

                # Volume options
                cls.master_volume = read_float(options, 'master_volume', cls.master_volume)
                cls.master_volume = clamp(cls.master_volume, 0, 1)
                cls.sound_volume = read_float(options, 'sound_volume', cls.sound_volume)
                cls.sound_volume = clamp(cls.sound_volume, 0, 1)
                cls.music_volume = read_float(options, 'music_volume', cls.music_volume)
                cls.music_volume = clamp(cls.music_volume, 0, 1)
    
        # Init sprite font
        SpriteFontManager.load_font('spr_font.png', '0123456789')

        # Init keyboard
        Keyboard.add('up', (K_UP, K_w))
        Keyboard.add('down', (K_DOWN, K_s))
        Keyboard.add('left', (K_LEFT, K_a))
        Keyboard.add('right', (K_RIGHT, K_d))
        Keyboard.add('interact', (K_e, K_RETURN, K_SPACE))
        Keyboard.add('any', (K_LEFT, K_a, K_RIGHT, K_d, K_UP, K_w))
        Keyboard.add('key_left', (K_LEFT, K_a))
        Keyboard.add('key_right', (K_RIGHT, K_d))
        Keyboard.add('key_shoot', (K_UP, K_w))
        Keyboard.add('key1_left', K_a)
        Keyboard.add('key1_right', K_d)
        Keyboard.add('key1_shoot', K_w)
        Keyboard.add('key2_left', K_RIGHT)
        Keyboard.add('key2_right', K_LEFT)
        Keyboard.add('key2_shoot', K_UP)
        Keyboard.add('pause', K_ESCAPE)

    @classmethod
    def save(cls):
        options = {}

        # Language options
        options['lang'] = cls.lang

        # Volume options
        options['master_volume'] = cls.master_volume
        options['sound_volume'] = cls.sound_volume
        options['music_volume'] = cls.music_volume

        if not os.path.exists('datafiles'):
            os.mkdir('datafiles')

        with open('datafiles/options.json', 'w', encoding='utf-8') as file:
            json.dump(options, file)
    
    @classmethod
    def state(cls):
        if cls.level == 1:
            return {
                'color': Colors.ENEMY,
                'shoot_delay': (50, 60),
                'balls': [
                    (125, 175, 10)
                ],
                'max_score': 3,
                'max_balls': 6,
                'music': 'bgm_stage2.ogg'
            }
        elif cls.level == 2:
            return {
                'color': Colors.KYRGOS,
                'shoot_delay': (40, 60),
                'balls': [
                    (125, 175, 10)
                ],
                'max_score': 3,
                'max_balls': 6,
                'music': 'bgm_stage3.ogg'
            }
        elif cls.level == 3:
            return {
                'color': Colors.QUADROPA,
                'shoot_delay': (30, 60),
                'balls': [
                    (125, 175, 10)
                ],
                'max_score': 3,
                'max_balls': 6,
                'music': 'bgm_stage3.ogg'
            }
        elif cls.level == 4:
            return {
                'color': Colors.LANDIUS,
                'shoot_delay': (30, 40),
                'balls': [
                    (125, 175, 10),
                    (65, 175, 10),
                    (185, 175, 10)
                ],
                'max_score': 3,
                'max_balls': 10,
                'music': 'bgm_stage6.ogg'
            }
        elif cls.level == 5:
            return {
                'color': Colors.ALOHA,
                'shoot_delay': (20, 40),
                'balls': [
                    (125, 175, 10),
                    (65, 205, 10),
                    (185, 145, 10),
                    (65, 115, 10),
                    (185, 235, 10)
                ],
                'max_score': 5,
                'max_balls': 10,
                'music': 'bgm_stage4.ogg'
            }
        elif cls.level == 6:
            return {
                'color': Colors.KEETESH,
                'shoot_delay': (10, 30),
                'balls': [
                    (125, 175, 10),
                    (65, 235, 10),
                    (185, 115, 10),
                    (65, 145, 10),
                    (185, 205, 10)
                ],
                'max_score': 5,
                'max_balls': 10,
                'music': 'bgm_stage4.ogg'
            }
        elif cls.level == 7:
            return {
                'color': Colors.KROTIK,
                'shoot_delay': (10, 20),
                'balls': [
                    (125, 175, 10),
                    (65, 205, 10),
                    (185, 145, 10),
                    (65, 115, 10),
                    (185, 235, 10)
                ],
                'max_score': 5,
                'max_balls': 10,
                'music': 'bgm_stage5.ogg'
            }