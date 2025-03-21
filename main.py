# Hangman game

import random
import pandas as pd

DATA_FILE = 'word_list.txt'
chances = 3

def random_word():
    df = pd.read_csv(DATA_FILE, header=None)
    df[0] = df[0].str.strip()
    word = random.choice(df[0].tolist())
    return word

def hint_msg(word):
    word_length = len(word)
    print("=== Welcome The Hangman Game ===")
    print(f"The word you are looking for has {word_length} letters!")


def get_answer(word,chances):
    word_length = len(word)
    letter_list = list(word)
    guessed_letters = [word[random.randint(0,word_length - 1)] if word else []]
    progress = [letter if letter in guessed_letters else '_' for letter in word]
    while chances > 0:
        print("\nCurrent status: ", " ".join(progress))
        print("Used letters: ", ", ".join(guessed_letters))
        print(f"Remaining attempts: {chances}")

        user_letter = input("Enter a letter: ").strip().lower()

        if user_letter in guessed_letters:
            print(f"{user_letter} Try another character, it's already in use.")
            continue

        guessed_letters.append(user_letter)

        if user_letter in letter_list:
            print(f"{user_letter} That's right!")
            for idx,letter in enumerate(word):
                if letter == user_letter:
                    progress[idx] = user_letter
        else:
            print(f"{user_letter} Not in the word.")
            chances -= 1

        if "_" not in progress:
            print("\nCongratulations! You have completed the word: ", word)
            return

    print("\nSorry! Your attempt has expired. True word: ", word)





def main():
    word = random_word()
    hint_msg(word)
    get_answer(word,chances)

if __name__ == "__main__":
    main()

