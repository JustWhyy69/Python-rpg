from ast import Pass


class Combat():
    def _init_(self, player_characters, npc, player_ply_function, endgame_function):
        self.player_characters = []
        self.npc = "monster.py"
        self.interactive_mode = True
        self.party_xp = 0
        self.party_success = True
        self.ordered_combatants = 0
        self.player_ply_function = ""
        self.endgame_function = ""
        
    def characters_dead(self):
         pass

    def combat_over(self):
        pass

    def combat_end(self):
        pass

    def ply(self):
        pass

    def print_status(self):
        pass

    def turn(self):
        pass

    def start(self):
        pass