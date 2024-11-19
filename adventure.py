def start_game():
    print("Hello adventurer, you are in a fairytale forest! choose your destiny wisely. You are in forest Entrance")
    player0neInput = input("Choose your Path: \n Path1: GO NORTH \n Path2: CLIMB OAK TREE...")
    if player0neInput == "GO NORTH":
        print("Looks like you didn't choose wisely, GAME OVER!!!!!")
        start_game()
    elif player0neInput == "CLIMB OAK TREE":
        print("You found a map, go west")
        west()
    else: 
        print("something wrong happend")
    



def west():
    print("Your are now facing two path! \n  ")
    player0neInput = input("Choose your Path and type as it is! \n Path1: PURPLE \n Path2: PINK...")
    if player0neInput == "PURPLE":
        print("You found Treature!!!")
    else:
        print("You got bitten by a poisonous spider")
        print("YOU LOST")
    while (player0neInput == "PINK"):
        print(west())
        break
print(start_game())

        










