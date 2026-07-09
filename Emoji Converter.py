
# If we want the string the user types as an input to be broken we use the split method .split().
#So the split method literally breaks the string by the words e.g. instead of "How are you" being just a string split
# makes the sentence seen as 3 strings to python like "How" + "are" + "you" instead of just one. it literally then makes it a list


# NOTE: this code below works well however it lacks a return value and hence cannot be reused in the code! the new code below this solves it!
# def emoji_converter(text):
#     words = text.lower().split(" ")
#     emojis = {
#         "happy": "😊",
#         "sad": "😢",
#         "joyful": "😎"
#     }
#     for word in words:
#         print(emojis.get(word, word), end=" ")
# message = input(">")
# emoji_converter(message)

# NOTE: this code solves the issue of return and allows this function to be used well and anywhere in the code!
def emoji_converter(text):
    words = text.lower().split(" ")
    emojis = {
        "happy": "😊",
        "sad": "😢",
        "joyful": "😎"
    }
    full_text = []
    for word in words:
        converted_words = emojis.get(word, word)
        full_text.append(converted_words)
    final_text = " ".join(full_text)
    return final_text


message = input("> ")
print(emoji_converter(message))
