num = [2, 2, 2, 5, 5]
letter = "x"

# METHOD 1(THE BEST AUTONOMOUS METHOD)
# for items in num:
#     items = items * "X"
#     print(items)
# METHOD 2( THIS IS SAME JUST USING A NESTED LOOP WHICH REALLY IS REDUNDANT, BUT GIVES SAME OUTPUT)
# for item in num:
#     for exes in letter:
#         exes = item * letter
#         print(exes)
# METHOD 3( THIS ONE IS HARDCODED AND LACKS AUTONOMY, BUT STILL GIVES RESULT!)
# for item in num:
#     if item == 5:
#         item = "xxxxx"
#         print(item)
#     if item == 2:
#         item = "xx"
#         print(item)
# METHOD 4( THIS METHOD USES NESTED LOOPS AND RANGE IN AN UNEXPEXTED WAY WHICH GIVES THE SAME RESULT)
for item in num:
    output = ""
    for count in range(item):
        output += letter
    print(output)


