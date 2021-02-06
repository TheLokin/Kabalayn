class GameObject(object):
    def __init__(self):
        self.groups = []

    def pre_update(self, events, *args):
        '''
            The pre_update method contains the code or actions that can be triggered by a game object.

            events: The list with the messages of the events.
        '''
        
        raise NotImplementedError('call to abstract method ' + repr(self.pre_update))
    
    def update(self, delta_time, *args):
        '''
            The update method contains the code or actions to be executed.

            delta_time: The time passed in microseconds between one update and another.
        '''
        
        raise NotImplementedError('call to abstract method ' + repr(self.update))

    def draw(self, surface, *args):
        '''
            The draw method governs what can be seen on the screen when the game is running.

            surface: The surface on which to draw.
        '''

        raise NotImplementedError('call to abstract method ' + repr(self.draw))

    def destroy(self):
        '''
            The game object is removed from all the groups that contain it.
        '''

        for group in self.groups.copy():
            group.remove(self)