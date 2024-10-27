'''Module is gonna test our Car class'''

import unittest

from unittesting_car_class import Car

class EasyTestCase(unittest.TestCase):
    '''Check out the basic functionality.'''

    def setUp(self):
        
        self.car = Car()

    def test_get_attribute(self):
        '''Does our car have all it needs to run?'''

        attributes = [
            "speed",
            "passengers",
            "turned_on",
            "max_passengers"]

        for attribute in attributes:
            self.car.get_attribute(attribute)

    def test_easy_one(self):
        '''Make sure the car can be started.'''
        self.car.turn_on()
        self.assertTrue(self.car.turned_on)

    def test_easy_two(self):
        '''Make sure the car can be turned off when running.'''
        self.car.turn_on()
        self.car.turn_off()
        self.assertFalse(self.car.turned_on)

    def test_easy_three(self):
        '''Can we add one passenger to the car?'''
        self.car.add_passengers(1)
        self.assertEqual(self.car.passengers, 1)

    def test_easy_four(self):
        '''Can we add four passenger to the car?'''
        self.car.add_passengers(4)
        self.assertEqual(self.car.passengers, 4)

    def test_easy_five(self):
        '''Can we add four passenger to the car and let two of them exit again?'''
        self.car.add_passengers(4)
        self.car.subtract_passengers(2)
        self.assertEqual(self.car.passengers, 2)

    def test_easy_six(self):
        '''Can we increase speed?'''
        self.car.increase_speed(4)
        self.assertEqual(self.car.speed, 4)

    def test_easy_seven(self):
        '''Can we decrease speed?'''
        self.car.increase_speed(4)
        self.car.decrease_speed(2)
        self.assertEqual(self.car.speed, 2)

    def tearDown(self):
        self.car = None
        

class MediumTestCase(unittest.TestCase):
    '''Now for some more juicy stuff!'''

    def setUp(self):
        self.car = Car()

    @unittest.skip("Engineers developed a car with unlimited seating.")
    def test_medium_one(self):
        '''Can we add more than max_passengers?'''
        with self.assertRaises(ValueError):
            crash_maximum_passengers = self.car.get_attribute("max_passengers") + 1
            self.car.add_passengers(crash_maximum_passengers)

    def test_medium_two(self):
        '''Can we let more people leave than are currently in the car?'''
        with self.assertRaises(ValueError):
            crash_minimum_passengers = self.car.get_attribute("passengers") + 1
            self.car.subtract_passengers(crash_minimum_passengers)

    def test_medium_three(self):
        '''Can somebody leave the car while driving?'''
        with self.assertRaises(RuntimeError):
            self.car.add_passengers(1)
            self.car.increase_speed(100)
            self.car.subtract_passengers(1)

    def tearDown(self):
        self.car = None

class HardTestCase(unittest.TestCase):
    '''And here we go shitting nuclear bricks into the engine.'''

    def setUp(self):
        self.car = Car()

    def test_hard_one(self):
        '''Can we add passengers to a moving car? I hope not!'''
        with self.assertRaises(RuntimeError):
            self.car.increase_speed(100)
            self.car.add_passengers(4)

    def test_hard_two(self):
        '''Ensure the ignition won't trigger when car is already running.'''
        
        with self.assertRaises(ValueError):
            self.car.turn_on()
            self.car.turn_on()

    def test_hard_three(self):
        '''Ensure the car can't be turned off when already off.'''
        with self.assertWarns(UserWarning):
            self.car.turn_off()
            self.car.turn_off()

    def tearDown(self):
        self.car = None
