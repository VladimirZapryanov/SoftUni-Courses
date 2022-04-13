<<<<<<< HEAD
from abc import abstractmethod, ABC


class Duck(ABC):
    pass


class RubberDuck(Duck):
    @staticmethod
    def quack():
        return "Squeek"

    @staticmethod
    def walk():
        """Rubber duck can walk only if you move it"""
        raise Exception('I cannot walk by myself')

    @staticmethod
    def fly():
        """Rubber duck can fly only if you throw it"""
        raise Exception('I cannot fly by myself')


class RobotDuck(Duck):
    HEIGHT = 50

    def __init__(self):
        self.height = 0

    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == self.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
=======
from abc import abstractmethod, ABC


class Duck(ABC):
    pass


class RubberDuck(Duck):
    @staticmethod
    def quack():
        return "Squeek"

    @staticmethod
    def walk():
        """Rubber duck can walk only if you move it"""
        raise Exception('I cannot walk by myself')

    @staticmethod
    def fly():
        """Rubber duck can fly only if you throw it"""
        raise Exception('I cannot fly by myself')


class RobotDuck(Duck):
    HEIGHT = 50

    def __init__(self):
        self.height = 0

    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == self.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
        self.height = 0