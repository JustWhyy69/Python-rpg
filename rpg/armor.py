import json

class Armor():
    def _init_(self):
        self.name = ""
        self.price = 0
        self.weight = 0
        self.ac = 0

    def load(self, path):
        with open(path) as f:
            weapon = json.load(f)
        print(weapon)
        self.name = weapon.get("name")
        self.price = weapon.get("price")
        self.weight = weapon.get("weight")
        self.ac = weapon.get("ac")