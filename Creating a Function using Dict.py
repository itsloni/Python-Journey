def translate_message(text):
    words = text.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "😢",
        ":<": "😎"
    }
    for word in words:
        print(emojis.get(word, word), end=" ")
    print()
user_message = input("Enter your message: ")
translate_message(user_message)
