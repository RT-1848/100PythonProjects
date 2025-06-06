print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")
path = input("You're at a cross road. Where do you want to go?\nType 'Left' or 'Right'\n")
road_path = path.lower()
if road_path == "right":
    print("You fell into a hole. Game Over...")
elif road_path == "left":
    path = input("You stumble upon a lake. What do you want to do?\nType 'Swim' or 'Wait'\n")
    swim_path = path.lower()
    if swim_path == "swim":
        print("You got attacked by trout. Game Over...")
    elif swim_path == "wait":
        path = input("A boat came and brought you to 3 doors.\nA yellow, blue, and red one.\nWhich one do you go through?\nType 'Yellow', 'Blue', or 'Red'\n")
        door_path = path.lower()
        if door_path == "yellow":
            print("Congratulations! You found the treasure!")
        elif door_path == "red":
            print("You got burned by fire. Game Over...")
        elif door_path == "blue":
            print("You were eaten by beasts. Game Over...")
        else:
            print("You did not choose the correct door. Game Over...")
    else:
        print("Wrong option. Game Over...")
else:
    print("Wrong option. Game Over...")