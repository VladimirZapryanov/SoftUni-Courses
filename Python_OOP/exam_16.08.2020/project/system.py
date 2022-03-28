from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"

        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware[0].install(express_software)
        System._software.append(express_software)

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"

        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware[0].install(light_software)
        System._software.append(light_software)

    @staticmethod
    def release_software_component(hardware_name, software_name):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        software = [s for s in System._software if s.name == software_name]
        if not hardware or not software:
            return "Some of the components do not exist"

        hardware[0].uninstall(software[0])
        System._software.remove(software[0])

    @staticmethod
    def analyze():
        return f"System Analysis\nHardware Components: {len(System._hardware)}\nSoftware Components: {len(System._software)}\nTotal Operational Memory: {sum([s.memory_consumption for s in System._software])} / {sum([h.memory for h in System._hardware])}\nTotal Capacity Taken: {sum([s.capacity_consumption for s in System._software])} / {sum([h.capacity for h in System._hardware])}"

    @staticmethod
    def system_split():
        result = ""
        for h in System._hardware:
            result += f"Hardware Component - {h.name}\n"
            result += f"Express Software Components: {len([s for s in h.software_components if s.software_type == 'Express'])}\n"
            result += f"Light Software Components: {len([s for s in h.software_components if s.software_type == 'Light'])}\n"
            result += f"Memory Usage: {sum(s.memory_consumption for s in h.software_components)} / {h.memory}\n"
            result += f"Capacity Usage: {sum(s.capacity_consumption for s in h.software_components)} / {h.capacity}\n"
            result += f"Type: {h.hardware_type}\n"
            if any([sc.name for sc in h.software_components]):
                result += f"Software Components: {', '.join([sc.name for sc in h.software_components])}\n"
            else:
                result += "None\n"
        return result.strip()
