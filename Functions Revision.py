# Converting this to a Function
comment = input("input an emoji with colon ':' and brackets ')' or '(' :> ")
comment_word = comment.split(" ")
comment_converter = {
    ":)" : "happy",
    ":(" : "sad"
}

output = ""
for word in comment_word:
    output += comment_converter.get(word, word) + " "

print("-----CHALLENGE 8-----")
print(f"{output}\n\n")

#How to use Functions
# It is basically used for pieces of code that will be needed or called/ reused multiple times such that when you
# call the function anywhere in your code it will, it will perform the tasks that u defined inside the function.

def greet_user(first_name, last_name):
    print(f"Hi there! {first_name} {last_name}")
    print("Welcome aboard")

print("Start")
greet_user("Loni", "Ayoola")
greet_user("Mary", "Magdalene")
print("Finish")

