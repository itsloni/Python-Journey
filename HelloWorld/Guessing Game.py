secret_number = 9
# guess = int(input("Guess: "))
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("Congratulations! You guessed the number!")
        break
else:
    print("Sorry! You lost the number!")

