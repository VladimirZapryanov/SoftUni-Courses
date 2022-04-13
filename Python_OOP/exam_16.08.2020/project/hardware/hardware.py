<<<<<<< HEAD
from project.software.software import Software


class Hardware:
    def __init__(self, name, hardware_type, capacity, memory):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.available_memory = memory
        self.available_capacity = capacity

    def install(self, software: Software):
        if self.available_memory < software.memory_consumption or self.available_capacity < software.capacity_consumption:
            raise Exception("Software cannot be installed")

        self.software_components.append(software)
        self.available_memory -= software.memory_consumption
        self.available_capacity -= software.capacity_consumption

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)


=======
from project.software.software import Software


class Hardware:
    def __init__(self, name, hardware_type, capacity, memory):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.available_memory = memory
        self.available_capacity = capacity

    def install(self, software: Software):
        if self.available_memory < software.memory_consumption or self.available_capacity < software.capacity_consumption:
            raise Exception("Software cannot be installed")

        self.software_components.append(software)
        self.available_memory -= software.memory_consumption
        self.available_capacity -= software.capacity_consumption

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)


>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
