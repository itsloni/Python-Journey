try:
    age = int(input('Age: '))
    print(age)
except ValueError: #This is the error exception that catches if the value is wrong. from the code above you see its int so
    #if the user then inputs a string normally its supposed to crash but then the exception prevents it from crashing and
    #then print what is below "Invalid Value" so the code run smoothly while telling us the error.
    print("Invalid Value")


#So here if we now have a calculation inside the code that has the chance to introduce another type of error other than value being wrong
#it will crash except we add another exception to catch that error. see below
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age # Now this is the calculation added now imagine the user inputs 0 as the age, You can see another error happens right?
    # cause 20000/0 is not possible mathematically.
    print(age)
except ZeroDivisionError: # Now you see the Exception needed to catch the error that would have crashed the 20000/0 yhh?
    print("Age cannot be 0.")
except ValueError:
    print("Invalid Value")