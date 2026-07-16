numbers = [1, 2, 4, 4, 4, 3, 4, 5]
numbers[0] = 20 #This is used to reasign or replace an item in a list using the index
print(numbers)

# numbers.append(6) #This method is used to add an item to the end of the list
# print(numbers)

# numbers.insert(1,5) # This method adds a number inbetween and the first number is the i
# # ndex position and the second is the number we want to add as shown below
# print(numbers)

# numbers.remove(5) # This method is Used to remove an item from a list
# print(numbers)

# numbers.clear() # This method doesn't take any values, and it's used to clear teh ENTIRE list
# print(numbers)

# numbers.pop() # This method is used to remove the very LAST item from a list
# print(numbers)

print(numbers.index(3))  # This method is used to return the index of the first appearance (if they're multiple) of that item in the list

print(numbers[0]) # This is used to check for the item in the numbers list that has the corresponding index.
print(30 in numbers) # This is also used to check for the existence of an item in the string. it gives a boolean response TRUE/FALSE

print(numbers.count(4)) # This is used to show the number of times and item appears in the list.

# numbers.sort() # This method Doesn't return any value so we print numbers after. it sorts the items in an orderly fashion.
# numbers.reverse() # what this does is after the sort method if u write it below, it reverses the sort so it's descending from big to small
# print(numbers) #It arranges it numerically. but cause the reverse lin eis above it prints it from reverse so big to small

numbers.copy() # This is used to make a copy of the numbers variable, however if any changes were made to the numbers variable
# the copy will not be affected. How to make a copy is:
numbers2 = numbers.copy()
numbers.append(300)
print(numbers2) # You will see that the numbers variable we appended with 300 will not show only the initial copy will show.