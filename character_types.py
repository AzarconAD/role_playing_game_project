from player_infos import PlayerInfos

class CharacterInfos(PlayerInfos):
    def __init__(self, health=100, armor=20, basic_attack=10, title="", name="", character_type=""):
        super().__init__(name, character_type)
        self.__health = health
        self.__armor = armor
        self.__basic_attack = basic_attack
        self.__title = title
        self.name = name
        self.char_type = character_type

    def is_alive(self):
        return self.__health > 0
    
    def status(self):
        print(f"{self.name} |Health: {self.__health}")

    def take_damage(self, amount):
        self.__health = max(0, self.__health - amount)

    def attack(self, enemy):
        damage = self.__basic_attack
        print(f"{self.name} attacks for {damage} damage.")
        enemy.take_damage(damage)

class Warrior(CharacterInfos):
    def __init__(self):
        super().__init__(armor=20)
        self.__title = "Mighty Warrior"

    def power_up(self):
        self.iron_shield_bonus = 30
        self.__armor += self.iron_shield_bonus

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
