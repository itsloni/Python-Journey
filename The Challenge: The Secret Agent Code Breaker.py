# You are writing a program for a secret agent. The agent will input a code made of numbers (like 102),
# and your program must translate it into a secret spy phrase.
# Your Tasks:
# 1.) Ask the user for a secret numeric code using input().
# 2.) Loop through the characters of that input.
# 3.) Convert each character to an integer.
# 4.) Print the matching spy word for each number horizontally on the same line with spaces in between.
# Example: If the user inputs 134, your program should print: Falcon At Midnight

spy_words = {
    0: "Red",
    1: "Falcon",
    2: "Flies",
    3: "At",
    4: "Midnight",
    5: "Danger",
}

secret_num = input("What's the Secret Numeric Code: ")
for code in secret_num:
    code = int(code)
    print(spy_words.get(code, "?"), end=" ")
