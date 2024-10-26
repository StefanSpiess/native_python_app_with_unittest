'''
So obviously we just gonna do this real quick (fuck I hate that guy by now)
and "this" is building a console application that prints out
information about profiles of some sort.
'''

class Profile():
    '''Some sort of profile.
    Has the following attributes:
    * age
    * job
    * name
    I guess the udemy teacher is just obsessed with bullshit.'''

    def __init__(self, age: int, job: str, name: str):
        self._age = age
        self._job = job
        self._name = name

    def print_age(self):
        '''Prints the age'''
        print(self._age)

    def print_job(self):
        '''Prints the job'''
        print(self._job)

    def print_name(self):
        '''Prints the name'''
        print(self._name)
