#course = "Python's Course for Beginners"
#print(course)
#To have a very long string lets say for like ann email and all,
# then a triple quote is needed (''' email contents here ''')
# and with that we can have text that spans multiple line that are sting strings
# Example
# course = '''
# Hi John,
#
# Here is our first email to you.
#
# Thank you,
# The support Team.
#
# '''
# print(course)

# course = 'Python for Beginners'
# print(course[2]) result is t

# course = 'Python for Beginners'
# print(course[-2]) result is r

# To Extract more than one character we make use of the colon : and the [] square brackets
# Note: the colon slices from the 0 to just before the 3
# or whichever index you want to slice to
# Example:
# course = 'Python for Beginners'
          # 01234
# print(course[0:3]) result = Pyt

#CHEAT SHEET : [START:STOP]

# and if it is left empty lik [0:] then it print all the indexed letters
# Example:
# course = 'Python for Beginners'
# print(course[:8])  # result = Python for Beginners

# Also if its print(course[:8]) the result will be (Python f).
# That tells me that it automatically assumes 0 index if left empty.
# Therefore, if its print(course[:]) it will print the entire course variable.
# result = Python for Beginners

# This also means that in a situation like this:
# course = 'Python for Beginners'
# another = course[:]
# and then we print the 'another' variable,
# we've basically made [:] the entire (Python for Beginners)
# print(another) result = Python for Beginners

course = 'Python for Beginners'
print(course[1:-1]) #The result will be (ython for Beginner),
# the P[0] and the s[-1] will not be added.





