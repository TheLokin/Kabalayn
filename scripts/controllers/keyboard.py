import pygame

from typing import Iterable
from .controller import Controller
from pygame.locals import KEYDOWN, KEYUP

def flatten(items):
    result = []

    for val in items:
        if isinstance(val, Iterable):
            result.extend(flatten(val))
        else:
            result.append(val)
    
    return result

class Keyboard(Controller):
    bindings = {}
    
    @classmethod
    def add(cls, name, *bindings):
        code = hash(name)

        if code in cls.bindings:
            raise Exception('Cannot repeat action name: ' + name)
        else:
            cls.bindings[code] = flatten(bindings)
    
    @classmethod
    def check(cls, name, events):
        code = hash(name)

        if code in cls.bindings:
            keys = pygame.key.get_pressed()

            for binding in cls.bindings[code]:
                if keys[binding]:
                    return True
            
            return False
        else:
            raise Exception('Unknown action name: ' + name)

    @classmethod
    def check_pressed(cls, name, events):
        code = hash(name)

        if code in cls.bindings:
            for event in events:
                if event.type == KEYDOWN and event.key in cls.bindings[code]:
                    return True
        
            return False
        else:
            raise Exception('Unknown action name: ' + name)

    @classmethod
    def check_released(cls, name, events):
        code = hash(name)

        if code in cls.bindings:
            for event in events:
                if event.type == KEYUP and event.key in cls.bindings[code]:
                    return True
        
            return False
        else:
            raise Exception('Unknown action name: ' + name)