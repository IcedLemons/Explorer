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

This is the database containing the player class for inventory, and interactions with objects.
"""
# =============================================================================
import place


# Player Class, contains user inventory and item take/drop commands.
class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def remove_all(self, item):
        if not self.inventory:
            print("You have no items")
            return
        print("\nDropping All Items")
        print("-------------------------------")
        for item in self.inventory:
            print(f"Dropped {item}")
            place.map.current_room.add_item(item)
        self.inventory.clear()


# Player name input
player = Player(input("Enter your name: "))
