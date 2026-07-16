
# TESTING THE CONCEPT.

try:
    f = open("file.txt")
    if f.name == "file.txt":
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as err:
    print(err)

else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")

    

# SO ESSENTIALLY BELOW IS HOW THE FOUR ARE TYICALLY USED AND HOW IT WORKS:

try:
    with open("file.txt", "r") as f:
        contents = f.read()
except FileNotFoundError: # This ONLY runs if the file is not found
    print("File not found.")
else: #This ONLY runs if the file is read with no errors successfully
    print("Success, File Clean")
    print(contents)
finally: # This part ALWAYS runs regardless or error or success.
    print("Operation Completed")

# SO LIKE IT ALL DEPENDS ON THE TRAJECTORY OF THE CODE AND PROBLEM YOUR SOLVING TO KNOW WHAT'S GONNA BE ON THE TRY OR ELSE BLOCK
# SO IF YOU WANNA ENSURE OPENING A FILE IS CORRECT THAT CAN BE PUT ALONE IN THE TRY BLOCK WHILE THE PRINTING IS DONE IN ELSE BLOCK
# IF IT DEALS WITH LIKE HUGE CALCULATIONS AND A LOT OF PRORBABILITIES PUTTING THE CODE IN THE TRY BLOCK SO PYTHON HAS THE OPPORTUNITY
# OF CHECKING THE EXCEPT FOR THOSE ERRORS SO IT DOESN'T CRASH OR ELSE IF IT'S IN THE ELSE BLOCK AND THEREA RE ERRORS IT WILL CRASH AND
# PRINT GIBBERISH ON THE TERMINAL NOT THE EXCEPTION THAT SHOULD HAVE BEEN PRINTED CAUSE THE CODE WERE IN THE ELSE BLOCK BELOW EXCEPTIONS.