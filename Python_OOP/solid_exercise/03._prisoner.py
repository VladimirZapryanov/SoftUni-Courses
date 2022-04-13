<<<<<<< HEAD
from abc import ABC, abstractmethod
import copy


class Person(ABC):
    @abstractmethod
    def __init__(self, position):
        self.position = position


class FreePerson(Person):
    def __init__(self, position):
        super().__init__(position)

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist


class Prisoner(Person):
    PRISON_LOCATION = [3, 3]

    def __init__(self):
        super().__init__(copy.copy(self.PRISON_LOCATION))


person = FreePerson([3, 3])
prisoner = Prisoner()
print("The prisoner trying to walk to north by 10 and east by -3.")

try:
    person.walk_north(10)
    person.walk_east(-3)
except:
    pass

print(f"The location of the prison: {prisoner.position}")
print(f"The current position of the prisoner: {prisoner.position}")

=======
from abc import ABC, abstractmethod
import copy


class Person(ABC):
    @abstractmethod
    def __init__(self, position):
        self.position = position


class FreePerson(Person):
    def __init__(self, position):
        super().__init__(position)

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist


class Prisoner(Person):
    PRISON_LOCATION = [3, 3]

    def __init__(self):
        super().__init__(copy.copy(self.PRISON_LOCATION))


person = FreePerson([3, 3])
prisoner = Prisoner()
print("The prisoner trying to walk to north by 10 and east by -3.")

try:
    person.walk_north(10)
    person.walk_east(-3)
except:
    pass

print(f"The location of the prison: {prisoner.position}")
print(f"The current position of the prisoner: {prisoner.position}")

>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
