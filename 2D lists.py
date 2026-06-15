matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# and in 2d list we can modify the matrix like saying:
# matrix[0][1] = 28 # the answer cause of this line will become 20 instead of printing 2
# print(matrix[0][1]) # it would print 2 normally but if that modification in the previous line
# was live it would print 28 not 2 cause it was modified

for row in matrix:
    for item in row:
        print(item)