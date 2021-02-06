from .object import GameObject

class Group(object):
    def __init__(self, *objects):
        self.objects = []

        self.add(*objects)

    def __iter__(self):
        return self.objects.__iter__()
    
    def __next__(self):
        return self.objects.__next__()

    def __contains__(self, obj):
        return self.objects.__contains__(obj)

    def __len__(self):
        return self.objects.__len__()

    def __lt__(self, other):
        return self.objects.__lt__(other)
    
    def __le__(self, other):
        return self.objects.__le__(other)

    def __eq__(self, other):
        return self.objects.__eq__(other)

    def __ne__(self, other):
        return self.objects.__ne__(other)

    def __gt__(self, other):
        return self.objects.__gt__(other)

    def __ge__(self, other):
        return self.objects.__ge__(other)

    def __hash__(self):
        return self.objects.__hash__()
    
    def __str__(self):
        return self.objects.__str__()

    def add(self, *objects):
        '''
            Adds a game object or sequence of game objects to the group.

            objects: The game object or game objects to add.
        '''

        for obj in objects:
            if isinstance(obj, GameObject):
                if not obj in self.objects:
                    obj.groups.append(self)
                    self.objects.append(obj)
            else:
                self.add(*obj)
    
    def remove(self, *objects):
        '''
            Removes a game object or sequence of game objects from the group.

            objects: The game object or game objects to remove.
        '''

        for obj in objects:
            if isinstance(obj, GameObject):
                if obj in self.objects:
                    obj.groups.remove(self)
                    self.objects.remove(obj)
            else:
                self.remove(*obj)
    
    def clear(self):
        '''
            Removes all the game objects from the group.
        '''

        for obj in self.objects.copy():
            obj.destroy()

    def pre_update(self, events, *args):
        '''
            The pre_update method contains the code or actions that can be triggered by all the
            game objects in the group.

            events: The list with the messages of the events.
        '''

        for obj in self.objects:
            obj.pre_update(events, *args)

    def update(self, delta_time, *args):
        '''
            The update method contains the code or actions that all the game objects in the group
            must execute.

            delta_time: The time passed in microseconds between one update and another.
        '''

        for obj in self.objects:
            obj.update(delta_time, *args)
    
    def draw(self, surface, *args):
        '''
            The draw method governs what can be seen on the screen when the game is running for all
            the game objects in the group.

            surface: The surface on which to draw.
        '''

        for obj in self.objects:
            obj.draw(surface, *args)