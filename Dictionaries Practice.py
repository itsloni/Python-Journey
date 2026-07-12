numbers = ["seven", "ten", "twenty", "five", "one", "six", "twenty", "seven", "ten", "five", "five", "one", "six", "twenty", "five", "six"]
sequence = {}

for num in numbers:
    if num not in sequence:
        sequence[num] = 0
    sequence[num] += 1
print(sequence)

numbers = [("seven", "7"),
           ("ten", "10"),
           ("twenty", "20"),
           ("five", "5"),
           ("one", "1"),
           ("twenty", "20"),
           ("seven", "7"),
           ("ten", "10"),
           ("five", "5"),
           ("five", "5"),
           ("one", "1"),
           ("six", "6"),
           ("twenty", "20")]
formatted = {}
for num, value in numbers:
    formatted[num] = value
print(formatted)

numbers = [("seven", "7"),
           ("ten", "10"),
           ("twenty", "20"),
           ("five", "5"),
           ("one", "1"),
           ("twenty", "20"),
           ("seven", "7"),
           ("ten", "10"),
           ("five", "5"),
           ("five", "5"),
           ("one", "1"),
           ("six", "6"),
           ("twenty", "20")]
formatted = {}
for num, value in numbers:
    if num not in formatted:
        formatted[num] = 0
    formatted[num] += 1
    if value not in formatted:
        formatted[value] = 0
    formatted[value] += 1

print(formatted)


numbers = [("seven", "7"),
           ("ten", "10"),
           ("twenty", "10"),
           ("five", "5"),
           ("one", "1"),
           ("twenty", "20"),
           ("seven", "7"),
           ("ten", "10"),
           ("five", "5"),
           ("five", "5"),
           ("one", "1"),
           ("six", "6"),
           ("twenty", "20")]
formatted = {}
for num, value in numbers:
    if num not in formatted:
        formatted[num] = {
            "occurrence": 0,
            "respective_num": []
        }
    formatted[num]["occurrence"] += 1
    formatted[num]["respective_num"].append(value)

print(formatted)



numbers = [("seven", "7"),
           ("ten", "10"),
           ("twenty", "10"),
           ("five", "5"),
           ("one", "1"),
           ("twenty", "20"),
           ("seven", "7"),
           ("ten", "10"),
           ("five", "5"),
           ("five", "5"),
           ("one", "1"),
           ("six", "6"),
           ("twenty", "20")]
formatted = {}
for num, value in numbers:
    if num not in formatted:
        formatted[num] = {
            "occurrence": 0,
            "respective_num": []
        }
    formatted[num]["occurrence"] += 1
    formatted[num]["respective_num"].append(value)
for key, value in formatted.items():
    print(f" This is the words: {key}, This is the occurrence and respective_num: {value}")
# To specify what you want inside the nested loop you just specify like this:
    print(f" This is the words: {key}, This is the occurrence and respective_num: {value["occurrence"]}")

