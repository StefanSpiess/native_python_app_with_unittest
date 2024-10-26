'''Module is gonna test our Profile class'''

import io
import unittest
from datetime import datetime

from unittesting_console_output import Profile


def hitlers_age_in_years_today() -> int:
    '''Always tells you the correct age of the Führer in years.'''
    aktuelles_jahr = datetime.now().year
    geburtsjahr = 1889
    alter = aktuelles_jahr - geburtsjahr
    return alter

AGE = hitlers_age_in_years_today()

class EasyTestCase(unittest.TestCase):
    '''Check out the basic functionality.'''

    def setUp(self):
        self.profile = Profile(AGE, "Dictator", "Adolf Hitler")

    def test_age_printer(self):
        '''Test if it returns the right age'''
        pass

    def test_job_printer(self):
        '''Test if it returns the right age'''
        pass

    def test_name_printer(self):
        '''Test if it returns the right age'''
        pass

    def tearDown(self):
        self.car = None
