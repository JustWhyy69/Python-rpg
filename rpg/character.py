class Character():
    def _init_(self):  
        self.name = "Player"
        self.strength = 0
        self.intelligence =0
        self.wisdom =0
        self.dexterity =0 
        self.constitution =0 
        self.charisma =0
        self.race = ""
        self.clas = ""
        self.level = 0
        self.max_hp = 0
        self.movement = 0
        self.armors =""
        self.weapons = ""
        self.xp =0
        self.type ="" 
        self.current_weapon = "fist"
        self.current_armor = ""
    
    def set_current_weapon(self):
        pass

    def roll_to_hit(self):
        pass

    def roll_for_damage(self):
        pass

    def get_ac(self):
        pass

    def get_movement(self):
        pass

    def get_ability_bonuses(self):
        pass