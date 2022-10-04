from rpg import character
from rpg import armor
from rpg import combat
from rpg import monster
from rpg import weapon

player1 = character()
player1.load_from_json("/charcters/Natilya.json")
player1.charisma = 14
player1.strength = 15

print(player1.name)
print(player1.charisma)