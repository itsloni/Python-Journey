# The Scenario
# You are writing the software for a bank ATM.
# The ATM has a specific amount of cash inside it, and a customer has a bank balance.
# You need to handle withdrawals and deposits securely while enforcing strict banking rules.
# The Starting VariablesStart your program with these three variables:
# atm_cash = 500         # The physical cash left inside the ATM machine
# user_balance = 300     # The money the user actually owns in their bank account
# pin_locked = True      # The user must unlock the ATM with a PIN first
# ==============================================================================
# STARTING VARIABLES
# ==============================================================================
# atm_cash = 500         # The physical cash left inside the ATM machine
# user_balance = 300     # The money the user actually owns in their bank account
# pin_locked = True      # The user must unlock the ATM with a PIN first

# ==============================================================================
# THE ATM RULES YOUR CODE MUST ENFORCE
# ==============================================================================
# 1. Unlocking the ATM (command: "unlock")
#    - If already unlocked: Tell them it's already unlocked.
#    - If locked: Ask for a PIN.
#    - If PIN is 1234: Unlock it (pin_locked = False).
#    - If PIN is wrong: Tell them and keep it locked.
#
# 2. Withdrawing Cash (command: "withdraw")
#    - Security Rule: If locked, refuse and tell them to unlock first.
#    - Balance Rule: If unlocked, ask for the amount. If amount is greater than
#      user_balance, refuse and say "Insufficient Funds".
#    - ATM Limit Rule: If amount is greater than atm_cash, refuse and say
#      "ATM out of cash".
#    - Success: Subtract amount from BOTH user_balance and atm_cash.
#      Print "Take your cash!".
#
# 3. Depositing Money (command: "deposit")
#    - Security Rule: Must be unlocked first.
#    - Success: Ask for amount. Add amount to user_balance.
#
# 4. Standard Commands
#    - "help": Print the rules.
#    - "exit": Break the loop.
# ==============================================================================
atm_cash = 500
user_balance = 300
pin_locked = True
prompt = ""
pin = ""
help = """
- To Unlock input unlock in the ATM machine
- To Withdraw input withdraw in the ATM machine
- To Deposit input deposit in the ATM machine
- To exit input exit in the ATM machine
- To get Help input help in the ATM machine """
# Your while True loop starts below here...
while True:
    prompt = input(">ATM Machine: ").lower()
    if prompt == "unlock":
            if pin_locked:
                while True:
                    pin = (input("Your PIN: "))
                    if pin == "1234":
                        print("ATM unlocked")
                        pin_locked = False
                        break
                    else:
                        print("Pin is Wrong, Input a correct PIN")
                        pin_locked = True
                        break
            else:
                print("ATM is already Unlocked")
                pin_locked = False
    elif prompt == "withdraw":
        if pin_locked:
            print("No! Unlock ATM first")
            pin_locked = True
        else:
            while True:
                amount = int(input("Amount to Withdraw: $").lower())
                if amount > user_balance:
                    print("Insufficient Funds")
                elif amount > atm_cash:
                    print("ATM out of Cash")
                elif amount <= user_balance:
                    print(f"Your withdrawal of ${amount} is SUCCESSFUL! Take Your Cash!")
                    user_balance -= amount
                    atm_cash -= amount
                    while True:
                        withdraw = input("Do you want to withdraw more money? (y/n): ").lower()
                        if withdraw == "y":
                            amount = int(input("Amount to Withdraw: $").lower())
                            if amount > user_balance:
                                print("Insufficient Funds")
                            elif amount > atm_cash:
                                print("ATM out of Cash")
                            elif amount <= user_balance:
                                print(f"Your withdrawal of ${amount} is SUCCESSFUL! Take Your Cash!")
                                user_balance -= amount
                                atm_cash -= amount
                        elif withdraw == "n":
                            print("Bye")
                            pin_locked = True
                            break
                        elif withdraw == "e":
                            break
                        elif withdraw != "y" and withdraw != "n":
                            print("Incorrect Input, Pls input y/n or Input 'e' to exit")
                        else:
                            break
                    break
    elif prompt == "deposit":
        if pin_locked:
            print("No! Unlock ATM first")
            pin_locked = True
        else:
            while True:
                adding = int(input("How much do you want to add?: $").lower())
                if adding < 1:
                    print("Type a sensible amount!")
                    break
                elif adding > 0:
                    print(f'Your New balance is $ {user_balance + adding}')
                    user_balance += adding
                    atm_cash += adding
                    while True:
                        more_add = input("Do you want to deposit more money? (y/n): ").lower()
                        if more_add == "y":
                            adding = int(input("How much do you want to add?: $").lower())
                            if adding < 1:
                                print("Type a sensible amount!")
                            else:
                                print(f'Your New balance is $ {user_balance + adding}')
                                user_balance += adding
                                atm_cash += adding
                        elif more_add == "n":
                            print("Bye")
                            pin_locked = True
                            break
                        elif more_add == 'e':
                            break
                        elif more_add != "y" and more_add != "n":
                            print(f"Incorrect Input, Pls y/n or Input 'e' to exit")
                        else:
                            break
                    break
    elif prompt == "help":
        print(help)
    elif prompt == "exit":
        break
    else:
        print("Input Correct Command: 'Unlock', 'Withdraw', 'Deposit', or 'Exit")
























