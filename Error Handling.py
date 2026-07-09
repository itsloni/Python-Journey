try:
    age = int(input("age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("Invalid value")
# More exceptions include:
# FileNotFoundError - for when files you call have been deleted or no longer exists
# KeyError - When the key called in the dictionary doesn't exist
# TypeError - when you like equate different datatypes like adding a string and an int
# IndexError - when you try to request an item from a specific position on a list. like requestion position 7 from a list with only 3 items
# requests.exceptions.Request.Exception - Network Error. This essentially is the error gotten due to like network crash or network errors