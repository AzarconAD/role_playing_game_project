class PlayerInfos:
    def __init__(self, name, character_type):
        self.__name = name
        self.__char_type = character_type

    def set_name(self, name):
        self.__name = name
        return self.__name
    
    def set_char_type(self, character_type):
        self.__char_type = character_type

