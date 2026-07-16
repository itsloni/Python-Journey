def calculator(value):
    nums = value.split(" ")
    my_digit_list = nums[0: : 2]
    my_symbol_list = nums[1: : 2]
    running_total = int(my_digit_list[0])
    for index, symbols in enumerate(my_symbol_list):

        my_next_digit = int(my_digit_list[index + 1])
        
        if symbols == "+":
           calc = running_total + my_next_digit
           running_total = calc
        elif symbols == "-":
            calc = running_total - my_next_digit
            running_total = calc
        elif symbols == "*":
            calc = running_total * my_next_digit
            running_total = calc
        elif symbols == "/":
            calc = running_total / my_next_digit
            running_total = calc
    return running_total
calculations = input("What do you want to Calculate?: ")
calculated_answer = calculator(calculations)
print(calculated_answer)
#
def quick_calculator(inputed):
    final = eval(inputed)
    return final

num_input = quick_calculator(input("What do you wanna Calculated?: "))
print(num_input)