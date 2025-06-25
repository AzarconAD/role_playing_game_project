from player_infos import PlayerInfos
from character_types import Warrior, Marksman, Tank
from game import Game
import json

def save_progress(player):
    data = {
        "name": player.name,
        "char_type": player.char_type,
        "health": player._CharacterInfos__health,
        "armor": player._CharacterInfos__armor,
        "basic_attack": player._CharacterInfos__basic_attack
    }
    with open("save_file.json", "w") as file:
        json.dump(data, file)

def load_progress():
    try:
        with open("save_file.json", "r") as file:
            data = json.load(file)

        if data["char_type"] == "Mighty Warrior":
            player = Warrior()
        elif data["char_type"] == "Skilled Marksman":
            player = Marksman()
        elif data["char_type"] == "Indestructable Tank":
            player = Tank()
        else:
            player = Warrior()

        player.name = data["name"]
        player.char_type = data["char_type"]
        player._CharacterInfos__health = data["health"]
        player._CharacterInfos__armor = data["armor"]
        player._CharacterInfos__basic_attack = data["basic_attack"]

        return player
    
    except FileNotFoundError:
        print("No saved game found.")
        return None

def main():
    name = input("Please enter your hero's name: ")
    player_infos = PlayerInfos(name, character_type="")
    player_infos.set_name(name)

    print("Choose your character type.")
    print("Choice 1: Warrior")
    print("Choice 2: Marksman")
    print("Choice 3: Tank")

    chosen_character = int(input("Your choice (1-3): "))

    if chosen_character == 1:
        player = Warrior()
        title = player.warrior_title()
        player_infos.set_char_type(title)

    elif chosen_character == 2:
        player = Marksman()
        title = player.marksman_title()
        player_infos.set_char_type(character_type=title)
    
    elif chosen_character == 3:
        player = Tank()
        title = player.tank_title()
        player_infos.set_char_type(character_type=title)

    print(f"Hero's name: {player_infos.set_name(name)}")
    print(f"Your character is the {player_infos.set_char_type(character_type=title)}!")

    game = Game(player)
    game.play()

if __name__=="__main__":
    main()