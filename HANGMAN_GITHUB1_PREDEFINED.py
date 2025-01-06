#!/usr/bin/env python
# coding: utf-8

# In[5]:



'''
🎮 Hangman Game 🎮
This is a Python implementation of the classic Hangman game with some enhancements:

- Players can choose the word length from predefined categories.
- A random word is selected from the chosen category.
- Players guess letters to uncover the word, with a limited number of guesses allowed.
- A scoring system rewards correct guesses and penalizes incorrect ones.
- The game can be replayed, and the total score is displayed at the end.

Features:
- Dynamic word selection from categories.
- User-friendly instructions and progress display.
- Case-insensitive input handling.
- Fun emojis to enhance the gameplay experience.

Have fun and test your word-guessing skills! 🧠✨
'''

import random

def initializeGame():
    '''
    Initialize the game by setting up word categories, allowing the user to choose a category,
    and randomly selecting a word for the player to guess.
    '''
    # Predefined word categories with extended words based on their length
    word_categories = {
        3: ['cat', 'bat', 'dog', 'fox', 'sun', 'cow', 'rat', 'owl', 'ant', 'bee'],
        4: ['lion', 'bear', 'wolf', 'frog', 'fish', 'deer', 'crow', 'duck', 'hawk', 'mole'],
        5: ['apple', 'grape', 'peach', 'chess', 'bread', 'plant', 'crowd', 'storm', 'sword', 'block'],
        6: ['yellow', 'planet', 'castle', 'forest', 'school', 'beauty', 'jungle', 'rocket', 'island', 'bridge'],
        7: ['teacher', 'pattern', 'quantum', 'example', 'journey', 'horizon', 'dolphin', 'emerald', 'fortune', 'serpent'],
        8: ['elephant', 'hospital', 'airplane', 'triangle', 'avocado', 'cherokee', 'mountain', 'wildfire', 'composer', 'sandwich']
    }

    # Display available word length categories to the user
    print("📚 Available Categories:")
    for length in word_categories.keys():
        print(f"📝 {length}-letter words")
    print("🔴 Enter '0' to exit.")

    # Allow the user to choose a category or exit
    while True:
        try:
            user_category_choice = int(input("👉 Choose the word length (3, 4, 5, 6, 7, 8) or '0' to exit: "))
            if user_category_choice == 0:
                return None, None, None  # Exit if the user chooses '0'
            elif user_category_choice in word_categories:
                listOfWords = word_categories[user_category_choice]
                break  # Valid category chosen, proceed
            else:
                print("❌ Invalid choice! Please choose a valid word length.")
        except ValueError:
            print("❌ Please enter a number.")

    # Randomly select a word from the chosen category
    secretWord = random.choice(listOfWords)

    # Create the hidden word (actual letters) and public display array (masked with underscores)
    hiddenArray = list(secretWord)
    publicArray = ["_" for _ in hiddenArray]

    return secretWord, hiddenArray, publicArray


def displayProgress(publicArray):
    '''
    Display the current progress of the guessed word, showing correctly guessed letters
    and underscores for letters yet to be guessed.
    '''
    print("📖 Current Progress: ", ' '.join(publicArray))


def updateHiddenWord(guess, hiddenArray, publicArray):
    '''
    Update the public display array with correctly guessed letters.
    '''
    for i in range(len(hiddenArray)):
        if hiddenArray[i].lower() == guess.lower():
            publicArray[i] = hiddenArray[i]


def checkWin(publicArray):
    '''
    Check if the player has successfully guessed the entire word.
    '''
    return "_" not in publicArray


def calculateScore(word_length, incorrect_guesses):
    '''
    Calculate the score based on the length of the word and penalties for incorrect guesses.
    '''
    base_score = word_length * 10  # Base score depends on word length
    penalty = incorrect_guesses * 2  # Each incorrect guess reduces the score
    return max(0, base_score - penalty)  # Ensure the score is not negative


def mainLoop():
    '''
    Main game loop to handle gameplay, scoring, and replay functionality.
    '''
    total_score = 0  # Initialize total score for the player

    while True:
        # Set up a new game round
        secretWord, hiddenArray, publicArray = initializeGame()
        if secretWord is None:  # Exit if the player chooses to quit
            print(f"🏁 Thanks for playing! Your total score is: {total_score} 🏆")
            break

        incorrectGuesses = []  # Keep track of incorrect guesses
        userGuesses = 0  # Count the total number of guesses made
        maxGuesses = len(hiddenArray) + 3  # Allow extra guesses beyond word length

        print(f"🎉 Welcome to Hangman! You have {maxGuesses} guesses to guess the word. 🤔")

        # Main gameplay loop for the current word
        while userGuesses < maxGuesses:
            guess = input("🔠 Enter your guess (uppercase or lowercase): ")

            if guess.lower() in [letter.lower() for letter in hiddenArray]:
                # Correct guess: update the display and check for a win
                updateHiddenWord(guess, hiddenArray, publicArray)
                print("✅ Your guess was correct!")
                displayProgress(publicArray)

                if checkWin(publicArray):
                    print(f"🎊 You win! The word was '{secretWord}'.")
                    score = calculateScore(len(hiddenArray), len(incorrectGuesses))
                    total_score += score  # Add the score for the current word to total score
                    print(f"🏅 Your score for this word is: {score}")
                    break
            elif guess.lower() in [letter.lower() for letter in incorrectGuesses]:
                # Prevent duplicate guesses
                print("⚠️ You've guessed that letter before, try a new one!")
            else:
                # Incorrect guess: update the incorrect guesses list and increment counter
                print("❌ Incorrect! Try again.")
                incorrectGuesses.append(guess.lower())
                userGuesses += 1
                print(f"🚨 Incorrect guesses: {userGuesses}/{maxGuesses}")

        if not checkWin(publicArray):  # Player loses if they fail to guess the word
            print(f"💀 Game over! The word was '{secretWord}'.")

        print(f"💼 Your total score so far is: {total_score}")
        print("-" * 40)

    # Display final score and exit message
    print(f"🏆 Final Score: {total_score}")
    print("Goodbye! 👋")


# Run the game
if __name__ == "__main__":
    mainLoop()


# In[ ]:




