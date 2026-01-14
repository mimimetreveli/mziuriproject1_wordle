
import random
from english_words import get_english_words_set

words=get_english_words_set(['web2'], lower=True)
five_letter_wordslists=[w for w in words if len(w) == 5]

def printasciiart(stage):
    if stage == 1:
        return """
┌─────┐
│ │
│ 😟
│
│
│
═══════════
"""
    elif stage == 2:
        return """
┌─────┐
│ │
│ 😟
│ │
│ │
│
═══════════
"""
    elif stage == 3:
        return """
┌─────┐
│ │
│ 😟
│ ╱│
│ │
│
═══════════
"""
    elif stage == 4:
        return """
┌─────┐
│ │
│ 😟
│ ╱│╲
│ │
│
═══════════
"""
    elif stage == 5:
        return """
┌─────┐
│ │
│ 😟
│ ╱│╲
│ │
│ ╱
═══════════
"""
    elif stage == 6:
        return """
┌─────┐
│ │
│ 😵
│ ╱│╲
│ │
│ ╱ ╲
═══════════
"""
print("Game rules: "
      "I choose a five letter word and you have to guess it, you can guess one "
      "letter per round or a whole word, if u guess a word u dont get another chance and either win or lose "
      "if you guess a letter and its in a word you get its posision, if not a body part is added to the rope "
      "and after 6 mistakes you lose.")
permision=input("Do you want to start/play again? ")
print(""""
┌─────┐
│ │
│
│
│
│
═══════════
""")
random_word = random.choice(five_letter_wordslists)
guess = ""
quit = "quit"
stage = 0
if permision == "yes":
    while guess != random_word:
        guess = input("Guess a letter: ")
        if guess.lower() == quit.lower():
            break
        if len(guess) == 1 and guess.lower() in random_word.lower():
            index = random_word.lower().index(guess.lower())+1
            print("your guess is in the word and its ",index,"th letter")
        elif len(guess) == 1:
            stage += 1
            if stage == 6:
                print("You lost, the word was ", random_word)
                break
            print(printasciiart(stage))
        elif len(guess) == 5:
            if guess.lower in random_word.lower():
                print("You WON!!")
                break
            else:
                print("You lost, the word was ",random_word)
                break
        elif guess.lower() not in quit.lower():
            print("invalid input")