# =====================================================================
# CHALLENGE: THE VIDEO GAME INVENTORY BUYER
# =====================================================================
#
# THE GOAL:
# You are coding an inventory system for an RPG game. The player
# is buying weapons from a shop. You need to update the player's
# current inventory dictionary with the weapons they bought.
#
# THE STARTING INVENTORY:
# Use this exact starting dictionary inside your function to hold
# the player's current weapon counts:
#
#
# THE RULES:
# 1. Create a function named 'buy_items' that accepts exactly ONE
#    parameter (a string of bought items).
# 2. The user will type the items they bought as a single sentence
#    separated by spaces (example: "sword potion potion shield").
# 3. Your function must break that sentence down into individual items.
# 4. For each item, update the count directly inside the 'inventory'
#    dictionary by adding 1.
# 5. If the player tries to buy something the shop doesn't carry
#    (meaning it's not already a key in the inventory, like "gun"),
#    ignore it completely.
# 6. Print the final updated 'inventory' dictionary.
#
# EXPECTED TEST:
# If the input typed is: sword potion gun potion shield
# The output printed must be: {'sword': 2, 'shield': 2, 'potion': 7}
# =====================================================================

def buy_items(items):
    inventory = {
        "sword": 1,
        "shield": 1,
        "potion": 5
    }
    words = items.split(" ")

    for word in words:
        if word in inventory:
            inventory[word] = inventory.get(word, 0) + 1
    print(inventory)

weapons = input("What weapons are you buying?  ")
buy_items(weapons)