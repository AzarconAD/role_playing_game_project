from player_infos import PlayerInfos
from character_types import Warrior
from character_types import Marksman

def main():
    player_infos = PlayerInfos()

    name = input("Please enter your hero's name: ")
    player_infos.set_name(name)

    print("Choose your character type.")
    print("Choice 1: Warrior")
    print("Choice 2: Marksman")

    chosen_character = int(input("Your choice (1-2): "))

    if chosen_character == 1:
        warrior = Warrior()
        title = warrior.warrior_title()
        player_infos.set_char_type(title)

    elif chosen_character == 2:
        marksman = Marksman()
        title = marksman.marksman_title()
        player_infos.set_char_type(title)

    print(f"Hero's name: {player_infos.set_name(name)}")
    print(f"Your character is the {player_infos.set_char_type(character_type=title)}!")

if __name__=="__main__":
    main()