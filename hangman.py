# Hangman
# Tejas Gokhale
# 2015-12-02

import string
import random
name = raw_input("Enter your name: ")
print "**** WELCOME TO HANGMAN, %s!" % name ," ****"
print "."
print "."
print "."

path = 'words.txt'

def load_words():
    print "Loading words from dictionary ..."
    wordFile = open(path, 'r', 0)
    line = wordFile.readline()
    wordList = string.split(line)
    print len(wordList), " words loaded from dictionary"
    return wordList

def choose_word(wordList):
    return random.choice(wordList)

def reveal_letter(hidden_word, word, user_input):
    for i in range(0, len(word)):
        if user_input == word[i]:
            hidden_word[i] = user_input
    return hidden_word

def hangman():
    wordList = load_words()
    word = choose_word(wordList).lower()
    word = list(word)
    length = len(word)
    print "Chappy is thinking of a word that is ... %d letters long. Guess away!" % length
    nGuess = 10
    hidden_word = '-'*length
    hidden_word = list(hidden_word)
    while(nGuess > 0):
        print "You have %d guesses left." %(nGuess)
        user_input = raw_input("Enter your guess: ")
        available = list("abcdefghijklmnopqrstuvwxyz")
        if user_input in available:
            hidden_word = reveal_letter(hidden_word, word, user_input)
        else:
            print "Invalid input. Please enter a letter."
        print ''.join(hidden_word)
        if hidden_word == word:
            print "You have guessed the word!"
            break
        if user_input in hidden_word:
            print "Good guess!"
        else:
            nGuess = nGuess - 1
        
    print "The word was %s" % ''.join(word)
    
hangman()    