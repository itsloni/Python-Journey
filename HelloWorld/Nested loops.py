# A Nested loop is basically having loop in a loop.
#WE an geerate a list if coordinates using nested loops.
for x in range(4):
    for y in range(3):
        print(f'({x}),({y})') # So in the for nested loop when the value of the x is zero and loops it enters y and that x value
        # completely loops through the for loop of y before it goes into the outer loop  and the value of x become
        # 1 and then it goes agin like that till it finishes, ultimately printing this: Below
        # (0),(0)
        # (0),(1)
        # (0),(2)
        # (1),(0)
        # (1),(1)
        # (1),(2)
        # (2),(0)
        # (2),(1)
        # (2),(2)
        # (3),(0)
        # (3),(1)
        # (3),(2)


