import random
item_drops = ["gold coin pouch", "silver dagger", "magic potion", "rusty sword", "healing herb"]
inventory = []

item = random.choice(item_drops)
inventory.append(item)
print(f"You have found a {item}.")

# To display the inventory
print("Your inventory:")
for item in inventory:
    print(f"- {item}")