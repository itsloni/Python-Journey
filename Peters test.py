print("Enter two integers, and i will tell you the relationship they satisfy: ")
number1 = int(input("Enter First Integer: "))
number2 = int(input("Enter Second Integer: "))

match (number1, number2):
    case(int1, int2):
        if int1 == int2:
            print("number1 is equals to number 2")
        elif int1 != int2:
            print("number1 is not equal to number2")
        elif int1 < int2:
            print("number1 is less than number2")
        elif int1 > int2:
            print("number1 is greater than number2")
        elif int1 <= int2:
            print("number1 is less or equal to number2")
        elif int1 >= int2:
            print("number1 is greater or equal to number2")





