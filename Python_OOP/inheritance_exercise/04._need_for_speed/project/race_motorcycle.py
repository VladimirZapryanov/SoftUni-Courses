<<<<<<< HEAD
from project.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8

    def __init__(self, fuel, horse_power):
=======
from project.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8

    def __init__(self, fuel, horse_power):
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
        super().__init__(fuel, horse_power)