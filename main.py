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
    print("Welcome to the RPG Battle Game!")
    print("1. New Game")
    print("2. Load Game")
    choice = input("Enter your choice: ")

    if choice == "2":
        player = load_progress()
        if player is None:
                return
    
    else:
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

        elif chosen_character == 2:
            player = Marksman()
            title = player.marksman_title()
        
        elif chosen_character == 3:
            player = Tank()
            title = player.tank_title()
        else:
            print("Invalid choice. Defaulting to Warrior.")
            player = Warrior()
            title = player.warrior_title()

        player.name = name
        player.char_type = title

        while True:
            print("\nWhat would you like to do next?")
            print("1. Play Battle")
            print("2. Use Skill / Magic")
            print("3. Save Game")
            print("4. Exit")
            next_choice = input("Enter choice: ")

            if next_choice == "1":
                game = Game(player)
                game.play()
            elif next_choice == "2":
                if isinstance(player, Warrior):
                    player.power_up()
                    print("Iron Shield activated! Your armor increased.")
                elif isinstance(player, Marksman):
                    player.power_up()
                    print("Critical Shot activated! Your basic attack increased.")
                elif isinstance(player, Tank):
                    player.power_up()
                    print("Rage Heal activated! Your health increased.")
            elif next_choice == "3":
                save_progress(player)
                print("Game progress saved!")
            elif next_choice == "4":
                print("Exiting game. Goodbye!")
                break
            else:
                print("Invalid option. Try again.")

    print(f"Hero's name: {player_infos.set_name(name)}")
    print(f"Your character is the {player_infos.set_char_type(character_type=title)}!")

    game = Game(player)
    game.play()

if __name__=="__main__":
    main()