from project.blade_knight import BladeKnight
from project.elf import Elf
from project.hero import Hero
from project.knight import Knight
from project.soul_master import SoulMaster
from project.wizard import Wizard

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)
wizard = Wizard("W", 5)
print(str(wizard))
knight = Knight("K", 10)
print(str(knight))
blade_knight = BladeKnight("BK", 2)
print(str(blade_knight))
soul_master = SoulMaster("SM", 14)
print((str(soul_master)))