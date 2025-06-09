
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


# Define Show Location Function, prompting whenever the player enters a new room.
def show_location():
    print(f"\n{player.location.name}")
    print(player.location.description)
    print("\nYou See The Following:")
    for item in player.location.items:
        print(item.name)
    print("\nExits:")
    for exit in player.location.exits:
        print(exit)

# Define game items here

#Living Room Items
flashlight = Item('Flashlight', "It's a brand new flashlight, batteries included.", True)
phone = Item("Phone", "A black rotary phone. There is no dial tone. No help is coming.", False)

# Dining Room Items
machete = Item("Machete", "A Sharp Machete. You bought it from the superstore but haven't really left your house to use it. It's well oiled and oddly sharp.", True)


# Hallway 1 and 2 items
pictures = Item("Pictures", "Pictures of yourself along with your family and friends", True)
bowl = Item("A Bowl", "A fruit bowl sitting on a small counter in the hallway. It holds random things like change and car keys.", False)
keys = Item("Keys", "The keys to the car in your garage. You're going to certainly need these.", True)


# Kitchen items
fridge = Item("Fridge", "A large, ancient fridge. It's gone warm since the power went out. You're afraid to open it.", False)
food = Item("Canned Goods", "A collection of all the non-perishable food in your kitchem, which isn't much. It's tucked into a crumbled superstore plastic bag.", True)

# Bedroom items
bed = Item("Your Bed", "A queen sized bed, neatly made with your favorite bedding set. While you long for rest, this is just not the time. Your Bug out Bag sits on the foot of the bed.", False)
bag = Item("Bug Out Bag", "It's a collection of clothes and tools you gathered hurriedly from your room. A Bug Out Bag you hurriedly threw together when the news first hit.", True)

# Bathroom Items
canteen = Item("Canteen", "A Canteen filled with cold water from the sink. You will need this wherever you go.", True)

# Define Rooms here and place items in it

# Living Room
living_room = Room("The Living Room", "It's been the same since you were a child. Calming except for the lack of electricity." )
living_room.items.append(flashlight)
living_room.items.append(phone)

# Hallway 1
hallway1 = Room(
    "A Long Hallway", # Totally just wanted to see if you could fstring when creating a class item
    f"The central hallway of your home. {pictures.description} line the walls. To your west is the kitchen and to your east is your dining room. North continues deeper into the house.")
hallway1.items.append(pictures)
# Hallway 2
hallway2 = Room("The End of The Hallway", "The hallway ends with the large exterior door to your garage. To the east is your bedroom, to the west is the bathroom.")
hallway2.items.append(keys)
# Bedroom
bedroom = Room("Your Bedroom", "The bed is made but your dressers and closer have been dug through. Everything worth taking is in your bug out bag laying on the bed.")
bedroom.items.append(bed)
bedroom.items.append(bag)
# Bathroom
bathroom = Room("The Bathroom", "It's a little dingy but completely functional. The water never got cut off even though the power is gone. A filled canteen sits on the sink.")
bathroom.items.append("canteen")
# Garage
garage = Room("The Garage", "This is it. Your car stands ready and you're ready to go. You take one last check of everything you gathered.")


# Kitchen
kitchen = Room("The Kitchen", "The kitchen is sparse, but it has everything you've needed up until the apocalypse. Some dishes lie unwashed in the sink. Probably not much reason to wash them now.")
kitchen.items.append(fridge)
kitchen.items.append(food)

# Dining Room
dining = Room("The Dining Room", "The dining room only contains a small table for eating and a singular chair. You spend a lot of time alone, sadly. Your computer desk and setup sit in the corner but are without power same as the rest of the house.")
dining.items.append(machete)



# Create room exits. Set them up in dictionaries rather than lists.
living_room.exits = {
    "north": hallway1}
hallway1.exits = {
    "south": living_room,
    "east": dining,
    "north": hallway2,
    "west": kitchen}
dining.exits = {
    "west": hallway1}
kitchen.exits = {
    "east": hallway1}
hallway2.exits = {
    "east": bedroom,
    "west": bathroom,
    "north": garage
}
bathroom.exits = {
    "east": hallway2
}




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
    print("You have to collect supplies and move to the garage at the far end of the house.")
    time.sleep(1)
    print("It's up to you to escape this nightmare. No help is coming.")
    time.sleep(1)
    print()


# Start the Initial Game Loop

#intro()
print(f"\n{player.location.name}")
print(player.location.description)
print("\nYou See The Following:")
for item in player.location.items:
    print(item.name)
else:
    print("There is nothing of value here.")
print("\nExits:")
for exit in player.location.exits:
    print(exit)


while True:
    command = input("> ").strip().lower()
    words = command.split()

    if len(words) == 0:
        show_location()
        continue

    verb = words[0]
    if len(words) > 1:
        noun = " ".join(words[1:])
    else:
        noun = None


    # Define Quit Command
    if verb == "quit":
        print("Thanks for playing!")
        break


    #Define Inventory command
    if verb in ["inv", "inventory"]:
        print("You have the following: ")
        for item in player.inventory:
            print(item.name)



    # Define Movement
    if verb in ["north", "south", "east", "west"]:
        if verb in player.location.exits:
            player.location = player.location.exits[verb]
            print(f"You go {verb} and find yourself {player.location.name}.")
            show_location()
        else:
            print("You cannot go that way!")

    # Define Examine Command
    elif verb == "examine" and noun:
        if noun == "room":
            print(f"\n{player.location.name}")
            print(player.location.description)
            print("\nYou see the following:")
            for item in player.location.items:
                print(item.name)
        else:
            found_item = next((item for item in player.location.items if item.name.lower() == noun.lower()), None)
            if found_item:
                print(found_item.description)
            else:
                print(f"There is no {noun} here.")

        continue

    # Define The Get Command
    elif verb == "get" and noun:
        found_item = next((item for item in player.location.items if item.name.lower() == noun.lower()), None)
        if found_item and found_item.is_movable:
            player.inventory.append(found_item)
            player.location.items.remove(found_item)
            print(f"You take the {noun}!")
        elif found_item and not found_item.is_movable:
            print("You simply can't take that.")
        else:
            print(f"There is no {noun} here.")
        continue

    # Define The Drop Command
    elif verb == "drop":
        for item in player.inventory:
            print("You drop the {}.".format(item.name))
            player.inventory.remove(item)
            player.location.items.append(item)

    # Define Exits Command
    elif verb.lower() == "exits":
        print("\nYou can see the following exits:")
        for direction in player.location.exits:
            print(f"- {direction} leads to {player.location.exits[direction].name}")
    else:
            print(f"{command} is not a valid command. Use 'Move', 'Examine', or 'Quit'.")

    if player.location.name == "garage":
        collected_items = len(player.inventory) # Adds up all found items
        if collected_items => 4:
            print("You step into the garage, breathing heavily as you try and work yourself up.")
            if "flashlight" in [item.name for item in  player.inventory]:
                print("The flashlight you rememebered illuminates the dark room, showing your car ready for you to leave.")
                


