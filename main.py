import random
import time
from loading_bar import printProgressBar

def main():
    
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
    
    print("Following the encounter with the goblins, you make your way to the town's tavern.")
    print("A weary looking farmer approaches you.")
    print("The farmer asks you to take care of a pack of wolves that have been terrorizing his livestock. Do you 'accept' or 'decline' this quest?")

    in_dialogue = True
    while in_dialogue:

        user_input = input(">").lower()

        if user_input == "accept":
            print("You follow the farmer back to his farm. He informs you that they usually attack at night. You take a seat and patiently wait until nightfall.")
            in_dialogue = False
        elif user_input =="decline":
            print("The farmer insists, and explains that he fears for his daughters safety.")
        else:
            print("Please select either 'accept' or 'decline'")

    print("As nightfall creeps across the farm and envelopes the farm, you hear howling in the near distance.")

    print("The wolves emerge from the surrounding darkness. You count a total of 3. You can take them...")

    items = list(range(0, 50))
    l = len(items)

    # Initial call to print 0% progress
    printProgressBar(0, l, length = 50)
    for i, item in enumerate(items):
        # Do stuff...
        time.sleep(0.3)
        # Update Progress Bar
        printProgressBar(i + 1, l, length = 50)

    in_wolf_encounter = True
    while in_wolf_encounter:
        print()
        user_input = input(">").lower()

main()
