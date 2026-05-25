pound = 0.45
kilo = 2.23

# Method 1 STYLE

weight = float(input("Weight: "))
weight_type = input("(L)bs or (K)g: ")
weight_p = weight * pound
weight_k = weight * kilo


if weight_type.lower() == "l":
    print(f"You're {weight_p} Kilograms")
elif weight_type.lower() == "k":
    print(f"You're {weight_k} Pounds")
else:
    print("Please enter a valid input")

# METHOD 2 STYLE

# weight = float(input("Weight: "))
# weight_type = input("(L)bs or (K)g: ")
#
# if weight_type.lower() == "l":
#     print(f"You're {weight * pound} kilograms")
# elif weight_type.lower() == "k":
#     print(f"You're {weight * kilo} pounds")
