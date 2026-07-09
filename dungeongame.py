print("You stand in the entrance hall of a dark castle. There are doors to your left and right.")
choice = input("Choose one of the options:\na) You go to the left door.\nb) You go to the right door. ").lower().strip()
match choice:
    case 'a':
        print("You walk towards a large table, a guard notices you.")
        print("You lose!")
    case 'b':
        print("You walk and find a small storage bunker.\nYou hear chattering up top, but feel light is so close.\nThere is a door to your right, and a small chamber upstairs.")
        choice2 = input("Choose one of the options\na) Go open the door.\nb) Climb upstairs. ").lower().strip()
        match choice2:
            case 'a':
                print("You see the brightness of the Sun yet again.\n You win!")
            case 'b':
                print("You confront the princess in her chambers.\nShe sends a peasant like you to the dungeon.\nYou lose!")
            case _:
                print("Invalid choice! You lose!")
    case _:
        print("Invalid choice! You lose!")

    

