def addition(value):
    split_value = value.split("+")
    adder = 0
    for num in split_value:
        if num.isdigit():
   


user_input = input("what do you want to add?: ")
print(addition(user_input))