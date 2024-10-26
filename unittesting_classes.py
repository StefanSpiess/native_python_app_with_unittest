'''Module with a class counting numbers. Hooray"'''

class Counter():
    '''What is this class gonna do? It is gonna count numbers.'''

    def __init__(self):
        self._value = 0

    def increment(self):
        '''Increments current value by one'''
        self._value += 1

    def decrement(self):
        '''Decrement current value by one'''
        self._value -= 1

    def reset(self):
        '''Reset current value to 0'''
        self._value = 0

    def get_value(self):
        '''Returns current value'''
        return self._value
