
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
        
