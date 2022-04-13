<<<<<<< HEAD
from math import floor
from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name, capacity, memory):
        super().__init__(name, "Power", floor(capacity * 0.25), floor(memory * 1.75))
=======
from math import floor
from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name, capacity, memory):
        super().__init__(name, "Power", floor(capacity * 0.25), floor(memory * 1.75))
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
