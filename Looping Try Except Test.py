# Here is your challenge. No hints, no hand-holding.
# ## The Scenario
# You are building a system for a logistics company. You have a list of packages.
# Each package is represented as a dictionary containing its ID, total weight,
# and the number of items inside that package.
# Your goal is to calculate the average item weight for each package.

# ## The Goal
# Write a loop that goes through this list and prints the average item weight for
# every single package that has valid data.
# Crucial Rule: Your code must handle the broken data entries gracefully using
# a try-except structure inside the loop. If one package hits an error, your
# script must not crash; it must print an error message for that specific package and
# immediately move on to process the next ones.

packages = [
    {"id": "PKG-01", "weight": 50, "items": 5},
    {"id": "PKG-02", "weight": 30, "items": 0},      # Someone made an entry mistake here!
    {"id": "PKG-03", "weight": "20", "items": 2},    # This weight was inputted as a string!
    {"id": "PKG-04", "weight": 45},                  # The "items" key is missing entirely!
    {"id": "PKG-05", "weight": 12, "items": 3}
]
for package in packages:
    try:
        for id, weight, items in package:
                if id in package:
                    if weight in package:
                        if items in package:
                            avg_item_weight = int(package["weight"]) / int(package["items"])
                            print(f'The average item weight is {avg_item_weight}')

    except ZeroDivisionError:
        print("Integer not divisible by Zero")
    except TypeError:
        print("Invalid Input")
    except KeyError:
        print("No key Present")

# for package in packages:
#     try:
#         for id, weight, items in package.items():
#             try:
#                 if id in package:
#                     try:
#                         if weight in package:
#                             try:
#                                 if items in package:
#                                     avg_item_weight = int(package["weight"]) / int(package["items"])
#                                     print(f'{package["id"]} has the average item weight of {avg_item_weight}')
#                             except KeyError:
#                                 print("Invalid Input")
#                             except ZeroDivisionError:
#                                 print("can't divide by Zero")
#                             else:
#                                 print(f'The average item weight is {avg_item_weight}')
#                     except TypeError:
#                         if not weight in package:
#                             print("Invalid Type")
#                     else:
#                         print(f'The average item weight is {avg_item_weight}')
#             except ValueError:
#                 if not id in package:
#                     print("Invalid Input")
#             else:
#                 print(f'The average item weight is {avg_item_weight}')
#     except ValueError:
#         print("Not correct value expectation")
#     else:
#         print(f'The average item weight is {avg_item_weight}')

        # except ZeroDivisionError:
        #     print("Integer not divisible by Zero")
        # except TypeError:
        #     print("Invalid Input")
        # except KeyError:
        #     print("No key Present")

else:
    print(f'The average item weight is {avg_item_weight}')









for package in packages:
    try:
        id = package["id"]
        items = package["items"]
        weight = package["weight"]
        avg_item_weight = int(weight) / int(items)
        print(f"{id} has the average item weight of {float(avg_item_weight)}")

    except TypeError:
        print("Invalid Input")
    except KeyError:
        print("Invalid Input")
    except ZeroDivisionError:
        print("can't divide by Zero")
    except ValueError:
        print("Invalid Value")



