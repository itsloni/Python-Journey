# --- VIP Club Checkout Practice Challenge ---

# 1. This is the list of ages waiting in line
ages = [15, 22, 18, 45, 12, 30]

# 2. Set up your counters here before the loop starts
allowed_guests = 0
total_revenue = 0

# 3. Write your for loop here to look at each age
for age in ages:
    if age >= 18:
        allowed_guests += 1
        total_revenue += 50

    # Hint: Add an IF statement here to check if the age is 18 or older
    # If they are allowed, add 1 to allowed_guests and add 50 to total_revenue
    #pass  # Delete this 'pass' line when you write your code!


# 4. Write your final print statements here (MAKE SURE THEY ARE NOT INDENTED!)
print(f"Total VIP guests allowed inside: {allowed_guests}")
print(f"Total ticket revenue collected: ${total_revenue}")
