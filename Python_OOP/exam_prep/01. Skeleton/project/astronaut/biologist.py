<<<<<<< HEAD
from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    def __init__(self, name):
        super().__init__(name, 70)

    def breathe(self):
        self.oxygen -= 5
=======
from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    def __init__(self, name):
        super().__init__(name, 70)

    def breathe(self):
        self.oxygen -= 5
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
