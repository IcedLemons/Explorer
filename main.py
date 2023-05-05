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

This is the database containing the list and dictionaries of rooms and items
"""
# =============================================================================
import place
import mc

# Actions list
actions = ["move", "look", "take", "drop", "inventory", "quit"]

"""
Spacer function used for aesthetics
"""


def spacer():
    print("===============================")


# Start the game
place.map.current_room = place.room1
spacer()
print(f"Welcome to the RPG Explorer {mc.player.name.title()}!")
print(place.map.current_room.description)
# Loops the game for continuous gameplay
while True:
    # Player Input
    spacer()
    for action in actions:
        print(f"- {action.title()}")
    print("\n")
    command = input("Select a Following action: ").lower()
    # Player movement
    if command == "move":
        spacer()
        direction = input("Select a direction (north, south, east, west) or quit: ").lower()
        if direction == "quit":
            print("\nThanks for playing!")
            break
        place.map.move(direction)
    # Look action to display room description and items within
    elif command == "look":
        spacer()
        print(place.map.current_room.description)
        if place.map.current_room.items:
            print("\n")
            print("You see the following items:")
            for item in place.map.current_room.items:
                print(f"- {item}")
    # Take an item from the current room and add to the player's inventory
    elif command == "take":
        if not place.map.current_room.items:
            print("There are no items in this room.")
            continue
        item_name = input("\nEnter the name of the item you want to take: ")
        if item_name == "quit":
            print("\nThanks for playing!")
            break
        for item in place.map.current_room.items:
            if item_name.lower() == item.name.lower():
                mc.player.add_item(item)
                place.map.current_room.remove_item(item)
                print("-------------------------------")
                print(f"You picked up {item}")
                break
        else:
            print("\nThat item is not in this room.")
    # Drop an item from the player's inventory and add to the current room
    elif command == "drop":
        if not mc.player.inventory:
            print("\nYou have no items in your inventory.")
            continue
        item_name = input("\nEnter the name of the item, drop all , or quit: ")
        if item_name == "quit":
            print("\nThanks for playing!")
            break
        for item in mc.player.inventory:
            if item_name.lower() == item.name.lower():
                mc.player.remove_item(item)
                place.map.current_room.add_item(item)
                print(f"\nYou dropped {item}")
                break
            else:
                print("\nThat item is not in your inventory")
        if item_name == "drop all":
            mc.player.remove_all(place.map.current_room)
    # User inventory
    elif command == "inventory":
        if not mc.player.inventory:
            print("\n")
            print("You have no items in your inventory.")
            print("\n")
        else:
            print("\nYour inventory:")
            print("-------------------------------")
            for item in mc.player.inventory:
                print(f"- {item}")
    # Quit the game
    elif command == "quit":
        print("Thanks for playing!")
        break
        # Handle invalid input
    else:
        print("\nInvalid action. Please try again.")
