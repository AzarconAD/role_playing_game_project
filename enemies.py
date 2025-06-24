from character_types import CharacterInfos

class Enemy(CharacterInfos):
    def __init__(self, health=100, armor=20, basic_attack=10):
        super().__init__(health, armor, basic_attack)

class Minion(Enemy):
    def __init__(self):
        super().__init__(health=100, armor=20, basic_attack=10)

class Boss(Enemy):
    def __init__(self):
        super().__init__(health=100, armor=20, basic_attack=10)

    def special_power(self):
        self.enhanced_health = 50
        self.__health += self.enhanced_health
        self.enhanced_armor = 5
        self.__armor += self.enhanced_armor
        self.enhanced_basic_attack = 5
        self.__basic_attack += self.enhanced_basic_attack



