import random
word_list = ["apple", "beautiful", "potato"]
live = 6
choosen_word = random.choice(word_list)
print(choosen_word)
display = []
for i in range(len(choosen_word)):
    display += '_'
print(display)
Game_Over = False
while not Game_Over:
    guess_letter = input("Guess a letter: ").lower()
    for i in range(len(choosen_word)):
        letter = choosen_word[i]
        if letter == guess_letter:
            display[i] = guess_letter
    print(display)
    if guess_letter not in choosen_word:
        live -= 1
        if live == 0:
            Game_Over = True
            print("You Lose")
        if '_' not in display:
            Game_Over = True
            print("You win")
