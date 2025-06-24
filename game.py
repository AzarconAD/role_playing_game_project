from enemies import Minion
from character_types import CharacterInfos


class Game:
    def __init__(self, player):
        player = CharacterInfos()
        self.player = player
        enemy = Minion()
        self.enemy = enemy

    def play(self):
        print("Battle Start!")
        while self.player.is_alive() and self.enemy.is_alive():
            self.player.status()
            self.enemy.status()

            self.player.attack(self.enemy)
            if self.enemy.is_alive():
                self.enemy.attack(self.player)

        if self.player.is_alive():
            print("\n🏆 You defeated the enemy!")
        else:
            print("\n💀 You were defeated...")

             
    