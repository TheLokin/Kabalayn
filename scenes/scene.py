from .director import Director

class Scene(object):
    def __init__(self):
        self.director = Director()

    def pre_update(self, events):
        '''
            The update method contains the code or actions that can be triggered by a scene.

            events: The list with the messages of the events.
        '''

        raise NotImplementedError('call to abstract method ' + repr(self.pre_update))

    def update(self, delta_time):
        '''
            The update method contains the code or actions to be executed.

            delta_time: The time passed in microseconds between one update and another.
        '''

        raise NotImplementedError('call to abstract method ' + repr(self.update))

    def draw(self, screen):
        '''
            The draw method governs what can be seen on the screen when the game is running.

            screen: The main surface.
        '''
        
        raise NotImplementedError('call to abstract method ' + repr(self.draw))