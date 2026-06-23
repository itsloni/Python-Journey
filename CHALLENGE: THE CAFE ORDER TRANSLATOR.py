# =====================================================================
# CHALLENGE: THE CAFE ORDER TRANSLATOR
# =====================================================================
#
# THE GOAL:
# Create a reusable function that takes a customer's sentence order
# and prints out the exact total cost of that order.
#
# THE RULES:
# 1. You must create a custom function that accepts exactly ONE parameter.
# 2. The user will type their full order as a single sentence (example: "coffee cake juice").
# 3. Your function must break that sentence down to find the individual items.
# 4. Your function must look up the price of each item and add them all together.
# 5. If a customer types a word that is not on the menu, it should cost 0.
# 6. The function must print the final calculated total number on the screen.
# 7. You must call the function from outside, passing the user's input variable across the bridge.
#
# EXPECTED TEST:
# If the input typed is: coffee cake juice
# The output printed must be: 15
# =====================================================================

def translated_message(order):
    menu = {
        "coffee": 5,
        "tea": 3,
        "cake": 4,
        "juice": 6
    }
    words = order.split(" ")
    order_list = {}
    for word in words:
        if word in menu:
            if word not in order_list:
                order_list[word] = menu[word]
            else:
                order_list[word] += menu[word]

    total = 0

    for price in order_list:
        total += order_list[price]
    print(f"{total}")

    # OR THE SHORTEST AND LIGHTEST WAY TO WRITE THE CODE ABOVE IS:
    # for word in words:
    #     total += menu.get(word, 0)
    # print(f"{total}")

request = input("What do you want to order? ")
translated_message(request)