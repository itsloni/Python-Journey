# The initial hardcoded method
for x in ["xxxxx", "xxxxx"]:
    print(x)
    for y in ["xx"]:
        print(y)
for z in ["xx"]:
    print(z)

    #or
# The data driven efficency method
numbers = [5, 2, 5, 2, 2]
for items in numbers:
    items =  "x" * items
    print(items)
