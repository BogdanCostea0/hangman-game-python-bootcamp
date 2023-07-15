# Hangman Game

import random as r

print("welcome to hangman game")

list_words = ['bee', 'beer', 'beekeeper', 'coke', 'vanilla', 'icecream'] # initialize the list of words

word = r.choice(list_words)  # pick a random word from the list
nr_lifes = len(word)  # calculate the number of hearts based on the lenth of the word
hidden_word = len(word) * '*'

word_list = list(word.strip())  # transform string to list
hidden_word_list = list(hidden_word.strip())

print(hidden_word_list)  # printing [*,*,...,*]


def charpositionreplace(word, char):   # finding the indexes of the letters and replacing in the hidden word list
    pos = []  # list to store position
    for n in range(len(word)):
        if word[n] == char:
            pos.append(n)
            hidden_word_list[n] = word[n]
    return pos


def verifyend(list, char):   # verify if the player has replaced all the '*' from the hidden list
    if char not in list:
        print("Good job, you nailed it!")
        return 0
    else:
        return 1


flag = 1
play = 1

while flag == 1 and play == 1:   # looping as long as there are hearts left and the game is not completed
    if nr_lifes == 0:
        print("Game Over")
        play = 0
        break
    else:
        letter = input("Guess a letter")   # asking for letter
        if letter in word_list:
            print("the letter is good")  # print for debug
            pos = charpositionreplace(word_list, letter)
            print(hidden_word_list)
            flag = verifyend(hidden_word_list, '*')
        else:
            nr_lifes -= 1
            print("You have ", nr_lifes, " hearts left.")





