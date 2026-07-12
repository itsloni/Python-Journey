# USING THE [] (BOX BRACKET) METHOD (So notice how this uses ONLY 2 lines of code!) well regardless their usage matters tho loni

shopping_dict = {
    "item_001": {"item": "apple", "price": 2},
    "item_002": {"item": "milk", "price": 3}
}
print(shopping_dict["item_001"]["item"], shopping_dict["item_001"]["price"])
print(shopping_dict["item_002"]["item"], shopping_dict["item_002"]["price"])

# USING THE.get() METHOD (Notice how this takes 6 lines of code compared to the [] method!)

item1a = shopping_dict.get("item_001", {}).get("item")
item1b = shopping_dict.get("item_001", {}).get("price")
print(item1a, item1b)

item2a = shopping_dict.get("item_002", {}).get("item")
item2b = shopping_dict.get("item_002", {}).get("price")
print(item2a, item2b)


# NOW EXTRACTING THEM FROM A LIST, THE DICTIONARIES.(Note that this is same as above dictionary just that this has index num as the key)
shopping_dict2 = [{"item": "apple", "price": 2},{"item": "milk", "price": 3}]

# USING THE [] (BOX BRACKET) METHOD
print(shopping_dict2[0]["item"], shopping_dict2[0]["price"])
print(shopping_dict2[1]["item"], shopping_dict2[1]["price"])

# USING THE.get() METHOD
dict_1a = shopping_dict2[0].get("item")
dict_1b = shopping_dict2[0].get("price")
print(dict_1a, dict_1b)

dict_2a = shopping_dict2[1].get("item")
dict_2b = shopping_dict2[1].get("price")
print(dict_2a, dict_2b)

# DELETING AND MODIFYING KEYS AND VALUES IN A DICTIONARY:
shopping_dict = {
    "item_001": {"item": "apple", "price": 2},
    "item_002": {"item": "milk", "price": 3}
}
shopping_dict["item_001"]["item"] = "banana" # MODIFYING THE VALUE HERE NOT KEY!
shopping_dict["item_002"]["stuff"] = shopping_dict["item_002"]["item"] # HERE I MODIFIED THE KEY not VALUE! FROM "item" to "stuff"
del shopping_dict["item_002"]["item"] # what you delete you cant print so you can't print item in item__002

print(shopping_dict["item_001"]["item"], shopping_dict["item_001"]["price"])
print(shopping_dict["item_002"]["stuff"], shopping_dict["item_002"]["price"])

# IF YOU WANT TO DELETE AN ITEM AND WANT A VARIABLE TO HAVE THE VALUE THE ITEM HAD, AND
# NOT THE VARIABLE REPLACING THE ITEM BUT THE VARIABLE JUST HAVING THE ITEMS VALUE, YOU USE .pop()
shopping_dict = {
    "item_001": {"item": "apple", "price": 2},
    "item_002": {"item": "milk", "price": 3}
}
new_variable = shopping_dict["item_002"].pop("price")
print(new_variable)