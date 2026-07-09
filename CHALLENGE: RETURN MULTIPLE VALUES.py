
# CHALLENGE: RETURN MULTIPLE VALUES
#
# 1. Create a function named get_multi_emojis that accepts two mood words as parameters.
# 2. Use a dictionary inside the function containing emoji mappings (e.g., happy, sad, joyful).
# 3. Look up both input mood words in the dictionary.
# 4. Return both found emojis simultaneously using a single return statement.
# 5. Outside the function, call get_multi_emojis and pass two different moods as arguments.
# 6. Assign the returned values into two separate variables at the same time.
# 7. Print both variables to confirm the function works correctly.


def get_multi_emojis(mood1, mood2):
    emojis = {
        "happy": "😊",
        "sad": "😢",
        "joyful": "😎"
    }
    # Write your code here


    words1 = mood1.split(" ")
    words2 = mood2.split(" ")

    converted_words1 = [emojis.get(word, word) for word in words1]
    converted_words2 = [emojis.get(word, word) for word in words2]
    fully_converted_word1 = " ".join(converted_words1)
    fully_converted_word2 = " ".join(converted_words2)

    return fully_converted_word1, fully_converted_word2


# final_output = get_multi_emojis("sad", "happy")
# This catches them into TWO separate variables!
# print(final_output)
choice1, choice2 = get_multi_emojis("sad", "happy")

print(choice1)
print(choice2)





# Write your function call here
# Print the results here
