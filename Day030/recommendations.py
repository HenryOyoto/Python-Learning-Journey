def main():
    difficulty = input("Difficult or Casual: ")
    if not (difficulty =="Difficult" or difficulty == "Casual"):
        print("Enter a valid difficulty level")
        return
   
    players = input("Multiplayer or Singleplayer: ")
    if not (players == "Multiplayer" or players == "Singleplayer"):
         print("Enter a valid number of players")
         return

    if difficulty == "Difficult" and players == "Multiplayer":
            recommend("FIFA 2026")

    elif difficulty == "Difficult" and players == "Singleplayer":
            recommend("Blus")

    elif difficulty == "Casual" and players == "Multiplayer":
            recommend("FIFA 2025")

    else:
            recommend("Roblox")

def recommend(game):
    print("I think you might like ", game)

main()