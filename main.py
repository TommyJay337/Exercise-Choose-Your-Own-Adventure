def main():
    import random
    
    print("Welcome to the Sword Coast. You're a traveler who's been in search of their next quest, so you head to the nearest tavern. On your way there, you stumble across a group of goblins on the road. Do you attempt to 'walk by' or 'fight'?")

    in_battle = True
    item_drops = ["gold coin pouch", "silver dagger", "magic potion", "rusty sword", "healing herb"]
    while in_battle:

        user_input = input(">").lower()

        if user_input == "fight":
            print(f"You successfully defeat the goblins in battle and find a {random.choice(item_drops)}")
            in_battle = False
        elif user_input == "walk by":
            print("The goblins block your path, and request that you hand over your belongings.")
            print("Will you now attempt to 'negotiate' or 'fight'?")
        else:
            print("Invalid input, please choose 'fight' or 'walk by'")

        user_input = input(">").lower()

        if in_battle and user_input == "negotiate":
            print("The goblins don't seem interested in talking and charge towards you.")
            print("What do you do? 'run' or 'fight'?")
        elif in_battle and user_input == "fight":
            print(f"You successfully defeat the goblins in battle and find a {random.choice(item_drops)}")
            in_battle = False

        user_input = input(">").lower()
        
        if in_battle and user_input == "fight":
            print(f"You successfully defeat the goblins in battle and find a {random.choice(item_drops)}")
            in_battle = False
        elif user_input == "run":
            print("Like a coward, you run from the encounter.")
            in_battle = False
    
    print("Following the encounter with the goblins, you make you way to the town's tavern.")
    print("A weary looking farmer approaches you.")

main()
