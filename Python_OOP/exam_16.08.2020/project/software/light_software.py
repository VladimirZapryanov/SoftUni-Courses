<<<<<<< HEAD
from project.software.software import Software
from math import floor


class LightSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, "Light", floor(capacity_consumption * 1.5), floor(memory_consumption * 0.5))
=======
from project.software.software import Software
from math import floor


class LightSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, "Light", floor(capacity_consumption * 1.5), floor(memory_consumption * 0.5))
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
