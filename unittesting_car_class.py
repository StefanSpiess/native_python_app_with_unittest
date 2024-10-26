'''This defines our most versatile car'''

import warnings

class Car():
    '''My shiny new car class.'''

    def __init__(self):
        self.turned_on = False
        self.speed = 0
        self.passengers = 0
        self.max_passengers = 4

    def get_attribute(self, attribute: str):
        '''Good old getter'''
        if hasattr(self, attribute):
            return getattr(self, attribute)

    def turn_on(self):
        '''Turns the car on.'''
        if self.turned_on is False:
            self.turned_on = True
        else:
            raise RuntimeError("The car is already turned on.")

    def turn_off(self):
        '''Turns the car off.'''
        if self.turned_on is True:
            self.turned_on = False
        else:
            warnings.warn("The object is already turned on.", UserWarning)

    def add_passengers(self, number: int):
        '''Adding passengers in a way so that they survive and also sit
        comfortably by not exceeding max_passengers'''

        if number in (0, None):
            raise ValueError("Zero or None passengers entered the car."
                             "Is that some sort of philosophical joke?")

        if number < 0:
            raise ValueError("We have a different method for adding "
                             "negative numbers of passengers. Thanks.")

        if self.speed != 0:
            raise RuntimeError("The car is moving! Are you crazy?")

        if (self.passengers + number) > self.max_passengers:
            raise ValueError(f"Sorry, the car only seats {self.max_passengers}")

        self.passengers += number

    def subtract_passengers(self, number: int):
        '''Adding passengers in a way so that they survive and also sit
        comfortably by not exceeding max_passengers'''

        if number in (0, None):
            raise ValueError("Zero or None passengers left the car. "
                             "Is that some sort of philosophical joke?")

        if number < 0:
            raise ValueError("We have a different word for subtracting"
                             " negative numbers of passengers. We call it \"adding\".")

        if self.speed != 0:
            raise RuntimeError("The car is moving! Are you crazy?")

        if (self.passengers - number) < 0:
            raise ValueError(f"Hm. There are only {self.passengers} people in the car."
                             " You can not make {number} people leave.")

        self.passengers -= number

    def increase_speed(self, number: float):
        '''Speed this shit up a bit!'''
        self.speed += number

    def decrease_speed(self, number: float):
        '''Slooooooow baby, slow"'''
        self.speed -= number
