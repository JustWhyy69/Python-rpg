import json

class Weapon():
    def _init_(self):
        self.name = "fist"
        self.price = 0
        self.weight = 0
        self.size = 0
        self.damageLow = 1
        self.damageHigh = 4
        
    def load(self, path):
        with open(path) as f:
            weapon = json.load(f)
        print(weapon)
        self.name = weapon.get("name")
        self.price = weapon.get("price")
        self.weight = weapon.get("weight")
        self.size = weapon.get("size")
        self.damageLow = weapon.get("damage")[0]
        self.damageHigh = weapon.get("damage")[1]


