# QUESTION:
# Your Goal: Write a for loop that automatically loops through
# this list and prints the item, the price, and the stock for
# each product using the .get() method.
shopping_list = [
    {"item": "apple", "price": 2, "stock": 10},
    {"item": "milk", "price": 3, "stock": 5},
    {"item": "bread", "price": 1.5, "stock": 8}
]
for dic in shopping_list:
    item = dic.get("item")
    price = dic.get("price")
    stock = dic.get("stock")
    print(f"Item: {item}, Price: {price}, Stock: {stock}")
