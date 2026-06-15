### Challenge: The VIP Waiting Room

#### Instructions
# 1. Do NOT use set().
# 2. Use a loop and dynamic list methods (like .append(), .insert(), etc.).
# 3. Write it cleanly without hardcoding any specific names.
#
# #### The Scenario
# You are running a VIP nightclub. You have a list of guests who arrived, but there is a problem:
# some people snuck in multiple times, and the group of VIPs arrived late and are stuck at the back of the line!
#
# #### Your Goal
# Take the original guest_list and create a final, clean list called vip_room that follows these three strict rules:
# 1. Remove all duplicates so everyone appears only once.
# 2. Keep the original arrival order for the regular guests.
# 3. Move the VIPs to the very front of the final list.
#
# #### Expected Output
# When you print vip_room, it must look exactly like this:
# ['VIP_Sarah', 'VIP_Mike', 'Alex', 'Ben', 'Chloe', 'Dan']

guest_list = ["Alex", "Ben", "Alex", "Chloe", "VIP_Sarah", "Ben", "Dan", "VIP_Mike", "Chloe"]
vip_room = []

vip_count = 0
for name in guest_list:
    if name not in vip_room:
        vip_room.append(name)
        if name.startswith("VIP_"):
            vip_room.remove(name)
            vip_room.insert(vip_count, name)
            vip_count += 1
print(vip_room)

