numbers = [2, 2, 2, 5, 5]
# star = "****"
# for x in star: #(My Method Hard coded)
#     for num in numbers:
#         fin = num * x
#         print(fin)
#     break


# or

for num in numbers: #(My tutors method How to actually parse data.)
    output = ''
    for x_count in range(num):
        output  += "x"
    print(output)
