# # if temperature is greater tha 30
#     it's hot day
# otherwise if it's less than 10
#     it's a cold day
# otherwise
#  it's neither hot nor cold

# temperature = 70
#
# if temperature == 30:
#     print("It's a hot day")
# else:
#     print("It's not a hot day")


#Practice Problem
# if name is less than 3 characters long
#     name must be at least 3 characters
# otherwise if it's more than 50 characters long
#     name can be a maximum of 50 characters
# otherwise
#     name looks good!

name = "Loni"

if len(name) < 3:
    print(f"{name} must be at least 3 characters long")
elif len(name) > 50:
    print(f"{name} can be a maximum of 50 characters")
else:
    print(f"Name looks good!")

