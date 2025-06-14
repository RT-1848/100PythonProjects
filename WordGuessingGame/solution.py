import random

instruments = ['piano', 'cello', 'clarinet', 'trombone', 'tuba', 'drums', 'guitar']

random_word = random.choice(instruments)
guessed = ['_'] * len(random_word)
user_attempts = 6

while user_attempts > 0:
    print("Your word: " + ' '.join(guessed))
    user_guess = input("Enter a letter: ")
    if user_guess in random_word:
        for i in range(len(random_word)):
            if guessed[i] == user_guess:
                print('You already guessed the letter, try again...')
            elif user_guess == random_word[i]:
                guessed[i] = user_guess
                print('Great Guess! Keep Going!')
            
    else:
        user_attempts -= 1
        print(f"Wrong letter, you have {user_attempts} attempts left")

    if '_' not in guessed:
        print("Congratulations, you got all the letters!!")
        print(f"Your word was {random_word}")
        break
    elif user_attempts <= 0:
        print("You have ran out of attempts...")
        print(f"Your word was {random_word}")
    print("\n")