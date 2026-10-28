while True:

    def calculator(value):
        split_value = value.split(" ")
        print(split_value)

        while "+" in split_value:
            location_of_addition = split_value.index("+")
            print(location_of_addition)
            split_value_addition = int(split_value[location_of_addition - 1]) + int(split_value[location_of_addition + 1])
            split_value[location_of_addition - 1:location_of_addition + 1] = [split_value_addition]

        while "-" in split_value:
            location_of_subtraction = split_value.index("-")
            split_value_subtraction = int(split_value[location_of_subtraction - 1]) - int(split_value[location_of_subtraction + 1])
            split_value[location_of_subtraction - 1:location_of_subtraction + 1] = [split_value_subtraction]

        while "*" in split_value:
            location_of_multiplication = split_value.index("*")
            split_value_multiplication = int(split_value[location_of_multiplication - 1]) * int(split_value[location_of_multiplication + 1])
            split_value[location_of_multiplication - 1:location_of_multiplication + 1] = [split_value_multiplication]

        while "of" in split_value:
            location_for_of = split_value.index("of")
            split_value_for_of = int(split_value[location_for_of - 1]) * int(split_value[location_for_of + 1])
            



        return split_value[0]

    user_input = input("what do you want to calculate?: ")
    print(calculator(user_input))



# cat = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# cat[0:8] = [10]
# print(cat)