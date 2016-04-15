# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "C:\py2\proyects\ProblemSet3\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    wordList = []
    for letter in secretWord:
        wordList.append(letter)

    for letter in lettersGuessed:
        if letter in wordList:
            wordList.remove(letter)

    if wordList == []:
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guess = ""

    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            guess = guess + secretWord[i]
        else:
            guess = guess + "_ "
            
    return guess


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    availableLetters = ""
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            availableLetters = availableLetters + letter
    
    return availableLetters

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

    lettersGuessed = []
    guesses = 8

    print "Welcome to the game Hangman!"
    print "I am thinking of a word that is {0} letters long.".format(len(secretWord))
    
    while (guesses >= 0):
        print "-------------"
        
        if isWordGuessed(secretWord, lettersGuessed):
            print "Congratulations, you won!"
            break
        if guesses == 0:
            print "Sorry, you ran out of guesses. The word was {0}.".format(secretWord) 
            break
        
        print "You have {0} guesses left".format(guesses)
        print "Available letters: {0}".format(getAvailableLetters(lettersGuessed))
        letter = raw_input("Please guess a letter: ")
        letter = letter.lower()
        
        if letter in lettersGuessed:
            print "Oops! You've already guessed that letter:",
            print getGuessedWord(secretWord, lettersGuessed)
        elif letter in secretWord:
            lettersGuessed.append(letter)
            print "Good guess:",
            print getGuessedWord(secretWord, lettersGuessed)
        else:
            lettersGuessed.append(letter)
            guesses = guesses - 1
            print "Oops! That letter is not in my word:",
            print getGuessedWord(secretWord, lettersGuessed)
    

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
