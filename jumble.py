import random
def play_word_jumble(list_of_words):
    random_word=random.choice(list_of_words)
    letters=list(random_word)
    random.shuffle(letters)
    jumbled="".join(letters)
    print("I have a shuffled word, try to guess it.")
    return jumbled, random_word
list_of_words=["math","science","history"]
jumbled, answer=play_word_jumble(list_of_words)
print(jumbled)
while True:
    guess=input("Guess a word: ")
    if guess=="quit":
        break
    elif guess==answer:
        print("Correct!")
        break
    elif guess!=answer:
        print("Incorrect!")
