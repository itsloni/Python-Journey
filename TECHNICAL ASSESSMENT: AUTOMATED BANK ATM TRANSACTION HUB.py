# ======================================================================
# TECHNICAL ASSESSMENT: AUTOMATED BANK ATM TRANSACTION HUB
# ======================================================================
#
# BACKGROUND
# You are developing the core control logic for a bank ATM terminal. The
# system needs to handle a single user session, manage their banking
# states, and protect against fraudulent card usage.
#
# INITIAL SYSTEM STATE
# When the ATM boots up, it must start with the following conditions:
# - The user's account balance starts at exactly 500 dollars.
# - The user is NOT logged in (unauthenticated).
# - The user has 0 failed PIN attempts.
#
# FUNCTIONAL REQUIREMENTS
# Implement an interactive control loop using standard input commands.
# The system must handle case-insensitive inputs and execute the
# following logic:
#
# 1. "login"
#    - If the user is already logged in, print: "You are already logged in."
#    - If the user is NOT logged in, prompt them for a PIN using a nested
#      input() call.
#      * If they type "1234", print: "Login successful!" and update their
#        state to logged in. Reset their failed attempts back to 0.
#      * If they type anything else, print: "Incorrect PIN." and add 1
#        to their failed attempts.
#        CRUCIAL SECURITY EDGE CASE: If the user reaches exactly 3
#        failed PIN attempts, print: "🚨 CARD BLOCKED. SYSTEM LOCKDOWN. 🚨"
#        and terminate the application execution instantly.
#
# 2. "withdraw"
#    - If the user is NOT logged in, print: "Access denied. Please login first."
#    - If the user is logged in, prompt them for an amount using a nested
#      input() call. Convert this input to an integer.
#      * If the amount is greater than their current balance, print:
#        "Insufficient funds!"
#      * If the amount is less than or equal to their balance, deduct
#        the money from their balance and print the new balance.
#
# 3. "balance"
#    - If the user is NOT logged in, print: "Access denied. Please login first."
#    - If the user is logged in, display their current account balance.
#
# 4. "logout"
#    - If the user is NOT logged in, print: "You are not logged in."
#    - If the user is logged in, update their state to logged out and
#      print: "Logged out successfully."
#
# 5. "exit"
#    - Gracefully break the control loop and terminate the program.
#
# 6. Invalid Input
#    - If the user types anything else, print an unrecognized command
#      error message.
#
# INTERVIEWER'S INSTRUCTIONS
# - Choose clean, positive boolean names to represent the "Active/On" states.
# - Be careful with data types! Money amounts from input() need to be
#   numbers, not strings, if you want to compare or subtract them.
# ======================================================================


logged_in = False
failed_pin_attempt = 0
account_balance = 500

while failed_pin_attempt < 3:
    atm_input = input("> ").lower()
    if atm_input == "login":
        if not logged_in:
            password = input("Enter your password: ")
            if password == "1234":
                print("login successful!")
                failed_pin_attempt = 0
                logged_in = True
            else:
                print("Incorrect PIN.")
                failed_pin_attempt += 1
        else:
            print("You're already logged in")
    elif atm_input == "withdraw":
        if not logged_in:
            print("Access denied. Please login first.")
        else:
            withdraw_amount = input("Enter withdraw amount: ")
            if withdraw_amount.isdigit():
                withdraw_amount = int(withdraw_amount)
                if withdraw_amount > account_balance:
                    print("Insufficient funds!")
                elif withdraw_amount <= account_balance:
                    cash_available = account_balance - withdraw_amount
                    account_balance = cash_available
                    print(f"Here is your Cash of ${withdraw_amount}. you have ${account_balance} left.")
            else:
                print("Invalid Amount.")
    elif atm_input == "balance":
        if not logged_in:
            print("Access denied. Please login first.")
        else:
            print(f"Your account balance is ${account_balance}.")
    elif atm_input == "logout":
        if not logged_in:
            print("You are not logged in")
        else:
            print("Logged out successfully.")
            logged_in = False
    elif atm_input == "exit":
        break
    else:
        print("Incorrect input.")

else:
    print(" CARD BLOCKED. SYSTEM LOCKDOWN. 🚨")




