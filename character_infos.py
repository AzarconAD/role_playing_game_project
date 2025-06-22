#custom character details
class Character:
    def __init__(self, name, health, character_type):
        self.__name = name
        self.__health = health
        self.__char_type= character_type


    def get_name(self):
        return self.__name

    def get_character_type(self):
        return self.__char_type

    def is_alive(self):
        return self.__health > 0

    def get_health(self):
        return self.__health