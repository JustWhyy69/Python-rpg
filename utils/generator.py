from rpg.character import Character
import random

class Generator():
    def _init_(self):
        pass

    def character(self):
        char = Character()
        char.hp_max = 6
        char.intelligence = random.randint(3,19)
        char.strength = random.randint(3,19)
        char.wisdom = random.randint(3,19)
        char.dexterity = random.randint(3,19)
        char.constitution = random.randint(3,19)
        char.charisma = random.randint(3,19) 
        char.race = random.choice(["Human", "Nymph", "Dwarf", "Elf"])
        char.p_class = random.choice(["Cleric", "Bard", "Paladin", "Druid"])
        char.level = random.randint(0,2)
        char.max_hp = random.randint(10,30)
        char.movement = random.randint(20,40)
        char.xp = random.randint(0,1000)
        return char