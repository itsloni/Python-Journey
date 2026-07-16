def calculator(value):
    nums = value.split(" ")


    while "(" in nums and ")" in nums:
        location_in_nums = nums.index("(")
        location_in_nums_2 = nums.index(")")
        num_in_bracket = nums[location_in_nums + 1: location_in_nums_2]
        joined_value = " ".join(num_in_bracket)
        calculated_joined_value = calculator(joined_value)
        nums[location_in_nums: location_in_nums_2 + 1] = [calculated_joined_value]


    while "of" in nums:
        location_in_nums = nums.index("of")
        num = float(nums[location_in_nums - 1]) * float(nums[location_in_nums + 1])
        nums[location_in_nums - 1:location_in_nums + 2] = [num]

    while "/" in nums:
        location_in_nums = nums.index("/")
        num = float(nums[location_in_nums - 1]) / float(nums[location_in_nums + 1])
        nums[location_in_nums -1:location_in_nums + 2] = [num]

    while "*" in nums:
        location_in_nums = nums.index("*")
        num = float(nums[location_in_nums - 1]) * float(nums[location_in_nums + 1])
        nums[location_in_nums - 1:location_in_nums + 2] = [num]

    while "+" in nums:
        location_in_nums = nums.index("+")
        num = float(nums[location_in_nums - 1]) + float(nums[location_in_nums + 1])
        nums[location_in_nums - 1:location_in_nums + 2] = [num]

    while "-" in nums:
        location_in_nums = nums.index("-")
        num = float(nums[location_in_nums - 1]) - float(nums[location_in_nums + 1])
        nums[location_in_nums - 1:location_in_nums + 2] = [num]

    return nums[0]

prompt = input("What do you want to Calculate?: ")
answer= calculator(prompt)
print(answer)
