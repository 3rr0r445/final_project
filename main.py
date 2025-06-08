
# Define a class to describe rooms. Set parameters to include name, description, exits, and items. 
# Set room exits and visable items to an empty dictionary and list.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

# Define a class for the player. Set parameters to include name and description and inventory.
# Set the room inventory as an empty list.
class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []


# Define a class for items. Set parameters to include name, description, and whether or not the item is movable.
class Item:
    def __init__(self, name, description, is_movable):
        self.name = name
        self.description = description
        self.is_movable = is_movable

# Define game items here
flashlight = Item('A Flashlight', "It's a brand new flashlight, batteries included.", True)

# Define Rooms here and place items in it
living_room = Room("The Living Room", "It's been the same since you were a child. Calming except for the lack of electricity.", )
living_room.items.append(flashlight)

# Create the player and assign starting point
player = Player("The Player", living_room)

# Create Game Introduction
def intro():
    print("Welcome to Travis' Zombie Survival Game!")
    print("Created by: Travis Duran")
    print("Special Thanks to: CodeinPlace and Stanford.")
    print("Also a huge thanks to my fellow students in my section!")
    print()
    input("Press Enter to Begin...")
    print("\n--------------------------------")
    time.sleep(1)
    print("The outbreak has begun. The news fell silent hours ago.")
    time.sleep(1)
    print("You called for help before the phones went down and have been waiting since.")
    time.sleep(1)
    print("You smell smoke and something else you can't quite place, something sweet and sickly.")
    time.sleep(1)
    print("Gunfire, screams—once constant. Now gone. The world outside is eerily still.")
    time.sleep(1)
    print("What you can vaguely hear from outside is the sound of shambling footsteps and moaning.")
    time.sleep(1)
    print("Escape is probably a pipedream at this point. You must collect resources in this house and get to the basement to await rescue.")
    time.sleep(1)
    print()


# Start the Initial Game Loop

#intro()
print(f"\n{player.location.name}")
print(player.location.description)
print("\nExits:")
for exit in player.location.exits:
    print(exit)



