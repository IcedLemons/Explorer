# ---------------------------------------------
# Title: Castle Dungeon Explorer
# Assignment: Object-Oriented Programming
# Class: CS 30kh./

# Date : 01/05/23
# Coders Name:  Ben Chu
# Version:'5.0'
# ---------------------------------------------
"""
Current Assignment: Object-Oriented Programming

This is the database containing a list of items and their descriptions.
"""
# =============================================================================
# Item class, contains item description and name
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name} - {self.description}"


# Items lists
sword = Item("Sword", "[ A sharp robust weapon for combat ]")
potion = Item("Potion", "[ A magical elixir that heals wounds ]")
shield = Item("Shield", "[ A protective gear to block enemy attacks ]")
shackles = Item("Shackles", "[ A set of shackles with not one spot of rust ]")
crown = Item("Crown", "[ A golden crown studded with gems found sitting on the throne ]")
map = Item("Map", "[ Tanned from the ages with locations filled with mystery ]")
