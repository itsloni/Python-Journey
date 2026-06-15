### Challenge: The Airline Overbooking Crisis

#### Instructions
# 1. Do NOT use set().
# 2. Use loops and dynamic list methods.
# 3. Keep it 100% data-driven (no hardcoded passenger names or fixed numbers).
#
# #### The Scenario
# You are writing software for an airport gate. A flight is severely overbooked. The airline has a master
# list of passengers in the order they bought tickets.
#
# However, two things happened:
# 1. The computer system glitched and accidentally duplicated some passengers.
# 2. The airline needs to prioritize "Economy_Plus" passengers over regular "Economy" passengers,
# but "First_Class" passengers must absolutely stay at the very, very front of the plane.
#
# #### Your Goal
# Take the passenger_list and create a final, clean list called boarding_line that follows these three strict rules:
# 1. Remove all duplicates entirely.
# 2. First_Class passengers must be at the very front (keeping their original order relative to each other).
# 3. Economy_Plus passengers come next (keeping their original order relative to each other).
# 4. Economy passengers go to the back (keeping their original order).

# ]
#
# #### Expected Output
# When you print boarding_line, it must look exactly like this:
# ['First_Class_Tunde', 'First_Class_Fatima', 'Economy_Plus_Amara', 'Economy_Plus_Zainab', 'Economy_John', 'Economy_Chidi']


passenger_list = [
    "Economy_John", "Economy_Plus_Amara", "First_Class_Tunde",
    "Economy_John", "Economy_Plus_Amara", "Economy_Chidi",
    "First_Class_Fatima", "Economy_Plus_Zainab", "First_Class_Tunde",
    "First_Class_Loni", "First_Class_lola"
]
boarding_line = []
first_class_count = []
economy_plus_count = []
economy_count = []

for name in passenger_list:
    if name.startswith("First_Class"):
        if name not in first_class_count:
            first_class_count.append(name)
    elif name.startswith("Economy_Plus"):
        if name not in economy_plus_count:
            economy_plus_count.append(name)
    elif name.startswith("Economy"):
        if name not in economy_count:
            economy_count.append(name)
# boarding_line = first_class_count + economy_plus_count + economy_count
# print(boarding_line)

# OR USE THE .extend() what this does Loni is that it Unpacks the items inside the collection
# and dumps them into the list one by one, keeping the list flat.
boarding_line.extend(first_class_count)
boarding_line.extend(economy_plus_count)
boarding_line.extend(economy_count)
print(boarding_line)