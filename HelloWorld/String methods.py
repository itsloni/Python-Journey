from gettext import find

course = "Python for Beginners"
#len() is a built in function used to count the total number of
# characters in a data and here in a string.
# print(len(course)) result = 20
# print(course.upper()) result = PYTHON FOR BEGINNERS
# print(course.lower()) result = python for beginners
#print(course.find('for')) #This finds the index of FIRST OCCURRENCE of
# that character. hence after printing the result = 0 cause that is the
# first index of the character in the course variable.

# print(course.replace("Beginners","Absolute Beginners")) #LETTERS CAN ALSO BE REPLACED
#Another type of method is .replace(), and it replaces a word and
# to do that you separate the old word to be replaced with the new
# word just by a comma and then you print. Result = Python for Absolute Beginners
#Note: .replace() is CASE SENSITIVE!

# To check the existence or sequence of a character in a string. An in operator is used.
# Example:
print("Python" in course) #result = True, but if it's not there or
# the character isn't in the correct case then it says False
#Note: in operator is CASE SENSITIVE!

# DIFFERENCE BETWEEN in operator and .find() is that
# the in operator gives a boolean value in the terminal (True/False),
# while .find() give the index of the character or sequence of characters

#print(course.title())