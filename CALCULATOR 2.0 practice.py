while True:

    def calculator(value):
        split_value = value.split(" ")


        while "(" and ")" in split_value:
            location_of_first_bracket = split_value.index("(")
            location_of_second_bracket = split_value.index(")")
            split_value_in_bracket = split_value[location_of_first_bracket + 1:location_of_second_bracket]
            join_value_in_bracket = " ".join(split_value_in_bracket)
            calculating_joined_value_in_bracket = calculator(join_value_in_bracket)
            split_value[location_of_first_bracket:location_of_second_bracket + 1] = [calculating_joined_value_in_bracket]

        while "of" in split_value:
            location_for_of = split_value.index("of")
            split_value_for_of = int(split_value[location_for_of - 1]) * int(split_value[location_for_of + 1])
            split_value[location_for_of - 1:location_for_of + 2] = [split_value_for_of]

        while "/" in split_value:
            location_of_division = split_value.index("/")
            split_value_division = int(split_value[location_of_division - 1]) / int(split_value[location_of_division + 1])
            split_value[location_of_division - 1:location_of_division + 2] = [split_value_division]

        while "*" in split_value:
            location_of_multiplication = split_value.index("*")
            split_value_multiplication = int(split_value[location_of_multiplication - 1]) * int(split_value[location_of_multiplication + 1])
            split_value[location_of_multiplication - 1:location_of_multiplication + 2] = [split_value_multiplication]

        while "+" in split_value:
            location_of_addition = split_value.index("+")
            split_value_addition = int(split_value[location_of_addition - 1]) + int(split_value[location_of_addition + 1])
            split_value[location_of_addition - 1:location_of_addition + 2] = [split_value_addition]

        while "-" in split_value:
            location_of_subtraction = split_value.index("-")
            split_value_subtraction = int(split_value[location_of_subtraction - 1]) - int(split_value[location_of_subtraction + 1])
            split_value[location_of_subtraction - 1:location_of_subtraction + 2] = [split_value_subtraction]


        return split_value[0]

    user_input = input("what do you want to calculate?: ")
    print(calculator(user_input))
