from rpg.weapon import Weapon
from rpg.character import Character
from rpg.armor import Armor
from utils.generator import Generator

#sword = Weapon()
#sword.load('weapons/sword.json')
#print(sword.name)

#chainmail = Armor
#chainmail.load('armor/chaonmail.json')
#print(chainmail.name)

#Natilya = Character()
#Natilya.load_from_json("characters/Natilya.json")
#print(Natilya.name, Natilya.strength)

generator = Generator ()
new_character = generator.character()
print(new_character.hp_max, new_character.intel)