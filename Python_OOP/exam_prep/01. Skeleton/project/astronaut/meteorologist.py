<<<<<<< HEAD
from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    def __init__(self, name):
        super().__init__(name, 90)

    def breathe(self):
        self.oxygen -= 15
=======
from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    def __init__(self, name):
        super().__init__(name, 90)

    def breathe(self):
        self.oxygen -= 15
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
