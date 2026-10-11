numbers = [1, 4, 3, 2, 4, 9, 5, 4, 4, 3, 4, 5]
# numbers[0] = 20 #This is used to reassign or replace an item in a list using the index
# largest_num = numbers[0] #Code to REMOVE THE LARGEST NUMBER IN A LIST
# for num in numbers:
#     if num > largest_num:
#         largest_num = num
# print(largest_num)
# print(numbers)
# no_repeat_list = [] # Tis does get the job doesn't but is incredibly inefficient in a long list over thousands
# for num in numbers:
#     if numbers.count(num) > 1 and num not in no_repeat_list:
#         no_repeat_list.append(num)
#     elif numbers.count(num) == 1 and num not in no_repeat_list:
#         no_repeat_list.append(num)
# print(no_repeat_list)
duplicates_removed = []
for num in numbers:
    if num not in duplicates_removed:
        duplicates_removed.append(num)
print(duplicates_removed)


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

# print(numbers.index(3))  # This method is used to return the index of the first appearance (if they're multiple) of that item in the list
#
# print(numbers[0]) # This is used to check for the item in the numbers list that has the corresponding index.
# print(30 in numbers) # This is also used to check for the existence of an item in the string. it gives a boolean response TRUE/FALSE
#
# print(numbers.count(4)) # This is used to show the number of times and item appears in the list.
#
# # numbers.sort() # This method Doesn't return any value so we print numbers after. it sorts the items in an orderly fashion.
# # numbers.reverse() # what this does is after the sort method if u write it below, it reverses the sort so it's descending from big to small
# # print(numbers) #It arranges it numerically. but cause the reverse lin eis above it prints it from reverse so big to small
#
# numbers.copy() # This is used to make a copy of the numbers variable, however if any changes were made to the numbers variable
# # the copy will not be affected. How to make a copy is:
# numbers2 = numbers.copy()
# numbers.append(300)
# print(numbers2) # You will see that the numbers variable we appended with 300 will not show only the initial copy will show.