# ---------------------------------------------
# Title: Castle Dungeon Explorer
# Assignment: Object Oriented Programming
# Class: CS 30
# Date : 01/05/23
# Coders Name:  Ben Chu
# Version:'5.0'
# ---------------------------------------------
"""
Current Assignment: Object-Oriented Programming

This is the database containing the descriptions for rooms, list of rooms and 
possible exits.
"""
# =============================================================================
import items


# Map class, sets players current room and changes with movement.
# Has "barriers" to prevent user from going off the map
class Map:
    def __init__(self):
        self.current_room = None
        self.rooms = {}

    def add_room(self, room):
        self.rooms[room.name] = room

    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.rooms[self.current_room.exits[direction]]
            print(self.current_room.description)
        else:
            print("You cannot go that way.")


# Room class, contains the rooms' description, possible directions to go
# after and the items within the room
class Room:
    def __init__(self, name, description, items=None, exits=None):
        self.name = name
        self.description = description
        self.items = items or []
        self.exits = exits or {}

    def __str__(self):
        return self.name

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)


# Rooms Lists
room1 = Room("Great Hall",
             "\nYou step into a large, impressive room with long wooden table, tapestries, suits of armor, "
             "and a fireplace. There are 4 corridors in each direction")
room2 = Room("Armory",
             "\nAs you proceed through the halls, the ending opens up to a large training area lined with gleaming "
             "weapons and potions. There are only 2 exits, the way you came or continuing forwards.")
room3 = Room("Throne Room",
             "\nThe doors open to reveal a lovely velvet carpet that lead up to a massive golden throne studded with "
             "gems lying dead center on the far back wall of the room. There are no other paths aside from where you "
             "entered.")
room4 = Room("Courtyard",
             "\nAs you back into the courtyard you're met with a sword in stone, vines and flowers grow around the "
             "castle grounds. The courtyard is lined with sky high walls, there is only going back.")
room5 = Room("Jail Cells",
             "\nThe musty scents of dust and cobwebs hit you as you push open the thick iron doors leading to the "
             "jail cells, you're greeted to the lonely sites of bared rooms with only a single window in each all "
             "lined with iron bars. You look around only to see no other paths.")
room6 = Room("Lower Dungeons",
             "\nYou begin to descend lower into the depths of the castle, the only light sources now illuminating "
             "your way is the wavering glow of lanterns lining the walls, what mysteries await down here? As you "
             "explore, you find that this room is endless with no exit aside from where you entered.")

# Add items to rooms
room1.add_item(items.sword)
room2.add_item(items.potion)
room2.add_item(items.shield)
room3.add_item(items.crown)
room5.add_item(items.shackles)
room6.add_item(items.map)

# Add exits to rooms
room1.exits = {"north": room2.name, "south": room4.name, "west": room5.name, "east": room6.name}
room2.exits = {"south": room1.name, "north": room3.name}
room3.exits = {"south": room2.name}
room4.exits = {"north": room1.name}
room5.exits = {"east": room1.name}
room6.exits = {"west": room1.name}

# Create map
map = Map()
map.add_room(room1)
map.add_room(room2)
map.add_room(room3)
map.add_room(room4)
map.add_room(room5)
map.add_room(room6)
