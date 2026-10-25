# Converting this to a Function
# comment = input("input an emoji with colon ':' and brackets ')' or '(' :> ")
def emoji_converter(emoji):
    emoji_splitter = emoji.split(" ")
    emoji_converter = {
        ":)" : "happy",
        ":(" : "sad"
    }
    output = ""
    for word in emoji_splitter:
        output += emoji_converter.get(word, word) + " "
    return output

print("-----CHALLENGE 8-----")
print(f"{emoji_converter("Hello I am very :) . Never :( . so don't be :( you hear? Be :) !")}\n\n") # or You can put the input inside
print(f"{emoji_converter(input("what do you want to convert? "))}\n\n")



#How to use Functions
# It is basically used for pieces of code that will be needed or called/ reused multiple times such that when you
# call the function anywhere in your code it will, it will perform the tasks that u defined inside the function.

def greet_user(first_name, last_name):
    print(f"Hi there! {first_name} {last_name}")
    print("Welcome aboard")

print("-----CHALLENGE Functions Practice-----")
print("Start")
greet_user("Loni", "Ayoola")
greet_user("Mary", "Magdalene")
print("Finish\n\n")


# How to create functions that return values using Functions
def square(number):
    return number * number

print("-----CHALLENGE Functions Return Practice-----")

print(square(5))