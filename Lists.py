# Write a program to find the largest number in a list.

# numbers = [100000, 8, 9, 894, 3, 33, 88, 100, 234, 2, 7, 8, 9, 10000, 123, 9032, 44]
# values = numbers[0]
# for num in numbers:
#     if not num > values:
#         num = values
# print(values)
import re
brac = input(">: ")
brac_split = re.split(r" \(|\) |", brac)

print(brac_split)

