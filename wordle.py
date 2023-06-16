import random
from collections import Counter
word_list = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
def get_secret_word():
    return random.choice(word_list)
def play_wordle():
    secret_word = get_secret_word()
    guesses = 0
    while guesses < 6:
        guess = input('Enter your guess: ')
        if guess == secret_word:
            print('Congratulations! You guessed the word in', guesses, 'guesses.')
            return
        else:
            guesses += 1
            if guesses == 6:
                print('Sorry, you are out of guesses. The secret word was', secret_word)
                return
            else:
                count = Counter(secret_word)
                correct = [secret_word[i] == guess[i] for i in range(len(guess))]
                correct_count = sum(correct)
                print('Correct:', correct_count)
                print('Incorrect:', len(guess) - correct_count)
                print('Letter frequency:', ', '.join(f'{count[l]}x {l}' for l in count))
play_wordle()
