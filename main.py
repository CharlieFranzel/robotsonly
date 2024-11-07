import random

# Character classes with attributes: Strength, Agility, and Magic
classes = {
    "Warrior": {"Strength": 18, "Agility": 12, "Magic": 6},
    "Mage": {"Strength": 6, "Agility": 12, "Magic": 18},
    "Rogue": {"Strength": 12, "Agility": 18, "Magic": 6}
}

# Enemy types with their stats: Health, Attack, and Defense
enemies = {
    "Goblin": {"Health": 20, "Attack": 4, "Defense": 2},
    "Troll": {"Health": 40, "Attack": 8, "Defense": 4},
    "Dragon": {"Health": 80, "Attack": 16, "Defense": 8}
}

# Items available in the game with their types and effects
items = {
    "Potion": {"Type": "Healing", "Effect": 10},
    "Sword": {"Type": "Weapon", "Damage": 6},
    "Shield": {"Type": "Armor", "Defense": 4}
}

# Story stages, each with a description, enemies, and items to be found
stages = {
    "Haunted Forest": {
        "Description": "You are in a haunted forest.",
        "Enemies": ["Goblin"],
        "Items": ["Potion"]
    },
    "Enchanted Castle": {
        "Description": "You are in an enchanted castle.",
        "Enemies": ["Troll"],
        "Items": ["Sword"]
    },
    "Bandit's Lair": {
        "Description": "You are in a bandit's lair.",
        "Enemies": ["Dragon"],
        "Items": ["Shield"]
    }
}

# Player attributes initialized with name, class, health, and inventory
player = {
    "Name": "",
    "Class": "",
    "Health": 100,
    "Inventory": []
}

# Function to create a character by choosing a class
def create_character():
    print("Choose a character class:")
    for class_name in classes:
        print(class_name)
    class_choice = input("> ")
    player["Class"] = class_choice
    player["Health"] = 100

# Function to explore a given stage, encountering enemies and finding items
def explore_stage(stage):
    print(stage["Description"])
    if stage["Enemies"]:
        enemy = random.choice(stage["Enemies"])
        print(f"You encountered a {enemy}!")
        combat(enemy)
    if stage["Items"]:
        item = random.choice(stage["Items"])
        print(f"You found a {item}!")
        player["Inventory"].append(item)

# Function to handle combat with an enemy
def combat(enemy):
    # Loop continues while both player and enemy are alive
    while player["Health"] > 0 and enemies[enemy]["Health"] > 0:
        print(f"\nYour Health: {player['Health']}")
        print(f"{enemy}'s Health: {enemies[enemy]['Health']}")
        action = input("What do you do? (Attack/Defend/Use Magic) > ")
        
        # Player chooses an action: Attack, Defend, or Use Magic
        if action.lower() == "attack":
            damage = random.randint(1, 10) + classes[player["Class"]]["Strength"]
            enemies[enemy]["Health"] -= damage
            print(f"You attacked {enemy} for {damage} damage!")
        
        elif action.lower() == "defend":
            defense = random.randint(1, 10) + classes[player["Class"]]["Agility"]
            enemies[enemy]["Health"] += defense
            print(f"You defended against {enemy}'s attack!")
        
        elif action.lower() == "use magic":
            magic = random.randint(1, 10) + classes[player["Class"]]["Magic"]
            enemies[enemy]["Health"] -= magic
            print(f"You used magic on {enemy} for {magic} damage!")
        
        else:
            print("Invalid action!")
        
        # Enemy's turn to attack if still alive
        if enemies[enemy]["Health"] > 0:
            enemy_damage = random.randint(1, 10) + enemies[enemy]["Attack"]
            player["Health"] -= enemy_damage
            print(f"{enemy} attacked you for {enemy_damage} damage!")
    
    # Outcome of the combat
    if player["Health"] <= 0:
        print("You died!")
    else:
        print(f"You defeated {enemy}!")

# Function to manage the player's inventory, allowing use or discard of items
def manage_inventory():
    print("\nYour Inventory:")
    for item in player["Inventory"]:
        print(item)
    action = input("What do you do? (Use/Discard) > ")
    
    if action.lower() == "use":
        item_choice = input("Which item do you want to use? > ")
        if item_choice in player["Inventory"]:
            if items[item_choice]["Type"] == "Healing":
                player["Health"] += items[item_choice]["Effect"]
                print(f"You used {item_choice} and healed {items[item_choice]['Effect']} health!")
            elif items[item_choice]["Type"] == "Weapon":
                print(f"You equipped {item_choice}!")
            elif items[item_choice]["Type"] == "Armor":
                print(f"You equipped {item_choice}!")
        else:
            print("Invalid item!")
    
    elif action.lower() == "discard":
        item
