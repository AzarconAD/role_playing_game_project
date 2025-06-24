class PlayerInfos:
    def __init__(self, name, character_type):
        self.name = name
        self.char_type = character_type

    def set_name(self, name):
        self.name = name
        return self.name
    
    def set_char_type(self, character_type):
        self.char_type = character_type
        return self.char_type
