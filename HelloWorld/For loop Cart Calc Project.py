# Write a program to calculate the total cost of all the items on a shopping cart.
prices = [1000, 20, 30, 20, 70, 10]
total = 0
num_products = 0 #This is optional you could just use len(prices) to get the total too since its moving through all the list in prices
prompt = ""
for items in prices:
    total += items
    num_products += 1
print(f"For the {num_products} Products in your cart, The Total Price is = {total}")
# or
# print(f"For the {len(prices)} Products in your cart, The Total Price is = {total}")












