numbers = [1, 5, 6, 7, 2, 8, 3, 23, 4, 5, 10, 6, 7, 39, 23, 4, 5, 10, 6, 7, 39, 9, 4, 8, 9, 7, 2, 3, 4, 10]
real_num = []
# for num in numbers:
#     if num not in real_num:
#         real_num.append(num)
# print(real_num)

#SHORTEST METHOD TO REMOVE DUPLICATES
numbers.sort()
# print(set(numbers)) Doing this will leave the numbers no longer in a list but a string asper curly brackets so list()
# is needed to convert it to a list back
re_list = list(set(numbers))
print(re_list)



