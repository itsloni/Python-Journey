numbers = {
    0 : "Zero",
    1 : "One",
    2 : "Two",
    3 : "Three",
    4 : "Four",
    5 : "Five",
    6 : "Six",
    7 : "Seven",
    8 : "Eight",
    9 : "Nine",
}
# value = input("Phone: ")
# for digit in value:
#     value = int(digit)
#     for key in numbers:
#         if key == value:
#             print(f"{numbers[key]}")

value = input("Phone: ")
for digit in value:
    digit = int(digit)
    print(f"{numbers[digit]}", end=" ")