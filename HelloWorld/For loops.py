# For loops are used to iterate over items of a collection such as a string.
# remember a string is a sequence of characters, so it looks like a collection.
# So we can use a for loop to iterate over each character in a string and do something
# about it.

# for item in 'Python':   #So in the first iteration item will be set to P, then
#     print(item)           # it will be looped and in the second iteration it will
                         # be set to y and so on like that.
 # Also list can be defined using square brackets []. list is
 # basically a list of items, names or whatever
# exmaple:
for item in ['Loni', 'John', 'Kehinde']:
    print(item)

#We could also lisy over a loop of numbers like:
for items in [1,2,3,4,7,8,9]:
    print(items)


# To loop between a range of numbers like imagine we wanted to loop up to 1000,
# Typing the numbers individually will be hectic so we use a function called range
#Example:
for items in range(10): # NOTE: When using range it doesn't print the last number
    print(items)      # in the range so 10 won't print just 1 - 9

# Now if you want  it to range between 2 numbers like from 20 to 39, you write range(20,39)
# and you guessed right the 39 won't print so that mean if you
# want 39 to print you range to 40, so 39 print and then if you want 40 to print you
# range 41 so 40 prints
#Example:
for items in range(20,39):
    print(items)
#Another thing is that with the range function, if you want the numbers
# printed to increase in steps like 2 to 4 etc just add it as the 3rd number range(2,10,2)
# meaning it will loop through 2 to 10 but oncrease steps by 2 printing 2, 4, 6, 8. VOILA
#example:
for items in range(2,10,2):
    print(items)
