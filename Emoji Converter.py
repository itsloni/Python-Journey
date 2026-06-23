
# If we want the string the user types as an input to be broken we use the split method .split().
#So the split method literally breaks the string by the words eg instead of "How are you" being just a string split
# makes the sentence seen as 3 strings to python like "How" + "are" + "you" instead of just one. it literally then makes it a list
message = input(">")
words = message.split(" ")
emojis = {
    ":)": "😊",
    ":(": "😢",
    ":<": "😎"
}
for word in words:
    print(emojis.get(word, word), end=" ")
