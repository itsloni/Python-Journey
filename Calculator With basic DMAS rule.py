
def calculator(value):
    print(value)
    nums = value.split(" ")

    print(nums)

    while "of" in nums:
        location_in_nums = nums.index("of")
        num = float(nums[location_in_nums - 1]) * float(nums[location_in_nums + 1])
        nums[location_in_nums - 1:location_in_nums + 2] = [num]
        print(nums)

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
