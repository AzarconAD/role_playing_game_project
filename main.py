from player_infos import PlayerInfos

def main():
    player_infos = PlayerInfos(name="", character_type="")

    name = input("Please enter your hero's name: ")

    print(f"Hero's name: {name}")
    print(player_infos.set_name(name))

if __name__=="__main__":
    main()