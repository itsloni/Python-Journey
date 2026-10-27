while True:

    def addition(value):
        split_value = value.split("+")
        adder = 0
        for num in split_value:
            if num.isdigit():
                # print(num)
                num = int(num)
                adder += num
            else:
                error = f"value is not a digit, please input a digit"
                return error
        return adder

    user_input = input("what do you want to add?: ")
    print(addition(user_input))