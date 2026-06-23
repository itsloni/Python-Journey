# =====================================================================
# 🚨 CHALLENGE: THE AUTOMATED SECURITY GUARD
# =====================================================================
# INSTRUCTIONS:
# 1. Complete the 'security_check' function to accept TWO parameters:
#    name and badge_num.
# 2. Inside the function, print the welcome messages.
# 3. Outside the function, ask the user for their inputs.
# 4. Call the function by passing your input variables into it.
# =====================================================================

# 1. Define your function here with two parameters
def security_check(name, badge_num):

    # print(f"Welcome {name}")
    # print(f"Checking badge number {badge_num}...")
    print(f"Welcome {name}, checking badge number {badge_num}...")

login = input("What is your name?: ")
login_2 = input("What is your badge number?: ")
security_check(login, login_2)



