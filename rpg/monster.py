class Monster():
    def _init_(self):
        self.name = "Beholder"
        self.type = "Aberration"
        self.ac = 18
        self.max_hp = 180
        self.movement = 20
        self.damage_low = 4
        self.damage_high = 24
        self.morale = "lawful evil"
        self.treasure_type = "rare"
        self.xp = 10000
    
    def roll_to_hit(self):
        pass

    def roll_for_damage(self):
        pass

    def get_ac(self):
        pass

    def get_movement(self):
        pass