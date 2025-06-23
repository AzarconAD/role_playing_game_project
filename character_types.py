class CharacterInfos:
    def __init__(self, health=100, armor=20, basic_attack=10, title=""):
        self.health = health
        self.armor = armor
        self.basic_attack = basic_attack
        self.title = title

class Warrior(CharacterInfos):
    def __init__(self):
        super().__init__(armor=20)
        self.title = "Mighty Warrior"

    def power_up(self):
        self.iron_shield_bonus = 30
        self.armor += self.iron_shield_bonus

    def warrior_title(self):
        return self.title