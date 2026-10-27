while True:

    def calculator(value):
        split_value = value.split(" ")

        while "+" in split_value:
            location_of_addition = split_value.index("+")
            split_value_addition = int(split_value[location_of_addition - 1]) + int(split_value[location_of_addition + 1])
            return split_value_addition

        while "-" in split_value:
            location_of_subtraction = split_value.index("-")
            split_value_subtraction = int(split_value[location_of_subtraction - 1] - split_value[location_of_subtraction + 1])
            return split_value_subtraction

    user_input = input("what do you want to calculate?: ")
    print(calculator(user_input))

