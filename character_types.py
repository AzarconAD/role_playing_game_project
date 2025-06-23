class CharacterInfos:
    def __init__(self, health=100, armor=20, basic_attack=10, title=""):
        self.__health = health
        self.__armor = armor
        self.__basic_attack = basic_attack
        self.__title = title

class Warrior(CharacterInfos):
    def __init__(self):
        super().__init__(armor=20)
        self.__title = "Mighty Warrior"

    def power_up(self):
        self.iron_shield_bonus = 30
        self.armor += self.iron_shield_bonus

    def warrior_title(self):
        return self.__title
    
class Marksman(CharacterInfos):
    def __init__(self):
        super().__init__(basic_attack=10)
        self.__title = "Skilled Marksman"

    def power_up(self):
        self.enhanced_basic_attack = 20
        self.__basic_attack += self.enhanced_basic_attack

    def marksman_title(self):
        return self.__title
    
class Tank(CharacterInfos):
    def __init__(self):
        super().__init__(health=100)
        self.__title = "Indestructable Tank"

    def power_up(self):
        self.health_regen = 200
        self.__health += self.health_regen

    def tank_title(self):
        return self.__title
