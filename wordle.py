
import random

five_letter_words = [
    'about', 'after', 'again', 'being', 'black', 'bring', 'build', 'catch',
    'chair', 'check', 'child', 'clear', 'close', 'could', 'doing', 'dream',
    'drive', 'early', 'eight', 'every', 'field', 'first', 'going', 'great',
    'green', 'group', 'happy', 'heart', 'horse', 'house', 'large', 'later',
    'learn', 'light', 'money', 'month', 'music', 'never', 'night', 'often',
    'order', 'other', 'place', 'point', 'quite', 'right', 'shall', 'short',
    'small', 'space', 'stand', 'start', 'still', 'table', 'thank', 'their',
    'there', 'these', 'thing', 'think', 'third', 'those', 'three', 'under',
    'watch', 'water', 'where', 'which', 'while', 'white', 'whole', 'woman',
    'world', 'would', 'write', 'wrong', 'young'
]

def printasciiart(stage):
    if stage == 1:
        return """
┌─────┐
│     │
│     😟
│
│
│
═══════════
"""
    elif stage == 2:
        return """
┌─────┐
│     │
│     😟
│     │
│     │
│
═══════════
"""
    elif stage == 3:
        return """
┌─────┐
│     │
│     😟
│    ╱│
│     │
│
═══════════
"""
    elif stage == 4:
        return """
┌─────┐
│     │
│     😟
│    ╱│╲
│     │
│
═══════════
"""
    elif stage == 5:
        return """
┌─────┐
│     │
│     😟
│    ╱│╲
│     │
│    ╱
═══════════
"""
    elif stage == 6:
        return """
┌─────┐
│     │
│     😵
│    ╱│╲
│     │
│    ╱ ╲
═══════════
"""
print("Game rules: "
      "I choose a five letter word and you have to guess it, you can guess one "
      "letter per round or a whole word, if u guess a word u dont get another chance and either win or lose "
      "if you guess a letter and its in a word you get its position, if not a body part is added to the rope "
      "and after 6 mistakes you lose.")
permission=input("Do you want to start/play again? ")
print(""""
┌─────┐
│     │
│
│
│
│
═══════════
""")
random_word = random.choice(five_letter_words)
guess = ""
quit = "quit"
stage = 0
if permission == "yes":
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
            if guess.lower() in random_word.lower():
                print("You WON!!")
                break
            else:
                print("You lost, the word was ",random_word)
                break
        elif guess.lower() not in quit.lower():
            print("invalid input")