def main():
    difficulty = input("Difficult or Casual: ")
    players = input("Multiplayer or Singleplayer: ")

    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("FIFA 2026")

        elif players == "Singleplayer":
            recommend("Blus")

        else:
            print("Enter a valid number of players")

    elif difficulty == "Casual":
        if players == "Multiplayer":
            recommend("FIFA 2025")

        elif players == "Singleplayer":
            recommend("Roblox")

        else:
            print("Enter a valid number of players")

    else:
        print("Enter a valid difficulty level")

def recommend(game):
    print("I think you might like ", game)

main()